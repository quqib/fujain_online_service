import sys
import types
import importlib
import unittest
from unittest import mock


def import_with_mocks():
    # Patch SessionLocal to return a mock session
    session_mock = mock.MagicMock(name="Session")

    def _session_factory():
        return session_mock

    # Create lightweight dummy model classes to capture init kwargs
    class _BaseModel:
        def __init__(self, **kwargs):
            self.kwargs = kwargs

    dummy_models = {
        'ServiceBasicInformationInfo': type('ServiceBasicInformationInfo', (_BaseModel,), {}),
        'ServiceBasicMarknetAccessInfo': type('ServiceBasicMarknetAccessInfo', (_BaseModel,), {}),
        'ServiceBasicSpecialSegmentInfo': type('ServiceBasicSpecialSegmentInfo', (_BaseModel,), {}),
        'ServiceBasicDutyInfo': type('ServiceBasicDutyInfo', (_BaseModel,), {}),
        'ServiceCounterServiceInfo': type('ServiceCounterServiceInfo', (_BaseModel,), {}),
        'ServiceOnlineProcessingInfo': type('ServiceOnlineProcessingInfo', (_BaseModel,), {}),
        'ServiceProcessingProcedureInfo': type('ServiceProcessingProcedureInfo', (_BaseModel,), {}),
        'ServiceAskedQuestionInfo': type('ServiceAskedQuestionInfo', (_BaseModel,), {}),
        'ServiceBasisHandlingInfo': type('ServiceBasisHandlingInfo', (_BaseModel,), {}),
        'ServiceApplicationMaterialInfo': type('ServiceApplicationMaterialInfo', (_BaseModel,), {}),
        'ServiceMaterialVerificationInfo': type('ServiceMaterialVerificationInfo', (_BaseModel,), {}),
    }

    # Build a fake package hierarchy for modelsCreate.modelsService.*
    pkg_root = types.ModuleType('modelsCreate')
    pkg_models_service = types.ModuleType('modelsCreate.modelsService')

    for name, cls in dummy_models.items():
        mod = types.ModuleType(f'modelsCreate.modelsService.{name}')
        setattr(mod, name, cls)
        sys.modules[f'modelsCreate.modelsService.{name}'] = mod
        setattr(pkg_models_service, name, mod)

    sys.modules['modelsCreate'] = pkg_root
    sys.modules['modelsCreate.modelsService'] = pkg_models_service

    # Patch storage.db.SessionLocal
    db_mod = types.ModuleType('storage.db')
    setattr(db_mod, 'SessionLocal', _session_factory)
    sys.modules['storage.db'] = db_mod

    # Now import the target module fresh to pick up our patches
    if 'storage.service_storage_message' in sys.modules:
        del sys.modules['storage.service_storage_message']
    mod = importlib.import_module('storage.service_storage_message')
    return mod, session_mock, dummy_models


class SaveServiceAllTests(unittest.TestCase):
    def setUp(self):
        self.mod, self.session_mock, self.dummy_models = import_with_mocks()
        # Reset call history per test
        self.session_mock.reset_mock(return_value=True, side_effect=True)

    def minimal_parsed(self):
        return {
            'service_basic': {
                'unid': 'U1',
                'basic_info_rowguid': 'BASIC_ROW',
                'infoprojid': 'IC', 'baseCode': 'BC', 'implCode': 'IMPL', 'taskHandleItem': 'TASK',
                'servicetype': 'S', 'addTypeName': 'IT', 'performLevelName': 'PL', 'lawlimit': 'LL',
                'promiseday': 'PD', 'promisdayinfo': 'PDI', 'deptname': 'DN', 'deptPropertyName': 'DPN',
                'deptEntrust': 'DE', 'coopOrg': 'CO', 'leadDept': 'LD', 'rightSourceName': 'RS',
                'contactphone': 'CP', 'monitorcomplain': 'MP', 'intermediaryServicesList': 'ISL',
                'resultName': 'RN', 'finishTypeName': 'FTN', 'resultFileType': 'RFT', 'resultFileName': 'RFN',
                'finishType': 'FT', 'finishGetTypeName': 'FGTN', 'finishInfo': 'FI', 'userType': 'UT',
                'enterif': 'E', 'handleForm': 'HF', 'sceneReason': 'SR', 'qiyeTheme': 'QT',
                'webApplyDegreeName': 'WAD', 'nearbyAreaName': 'NAN', 'countLimit': 'CL', 'nearbyInstruction': 'NI',
                'highFrequencyKstb': 'HF', 'kstbModel': 'KM', 'kstbOutAreaname': 'KOA',
                'planEnableDate': 'PED', 'planCancelDate': 'PCD', 'isSubscribeService': 'IRS', 'terminalSupport': 'T',
                'personalThemeCategory': 'PTC', 'companyThemeCategory': 'CTC', 'mobileSingleLogin': 'MSL',
                'pcSingleLogin': 'PSL', 'smallTownsName': 'TSN', 'smallTownsCode': 'TSC', 'communityName': 'CN',
                'communityCode': 'CC', 'logisticsExpress': 'LE', 'onlinePay': 'OP', 'state': 'ST',
                'agentFlag': 'AF', 'chargeLimit': 'CH', 'iremark': 'IR', 'dirLink': 'DL'
            }
        }

    # 1. Should add basic info and commit when only required data provided
    def test_commit_with_minimal_data(self):
        data = self.minimal_parsed()

        self.mod.save_service_all(data)

        self.session_mock.add.assert_called()
        self.session_mock.commit.assert_called_once()
        self.session_mock.close.assert_called_once()

    # 2. Should rollback and re-raise on SQLAlchemyError
    def test_rollback_on_sqlalchemy_error(self):
        data = self.minimal_parsed()

        class DummyErr(Exception):
            pass

        # Patch SQLAlchemyError in module to our dummy for the test
        with mock.patch.object(self.mod, 'SQLAlchemyError', DummyErr):
            self.session_mock.add.side_effect = DummyErr('boom')
            with self.assertRaises(DummyErr):
                self.mod.save_service_all(data)
            self.session_mock.rollback.assert_called_once()
            self.session_mock.close.assert_called_once()

    # 3. Should insert special segments list items
    def test_inserts_special_segments(self):
        data = self.minimal_parsed()
        data['service_section_list'] = [
            {'sname': 'A', 'sday': '1', 'sconent': 'B', 'sremark': 'C'},
            {'sname': 'X', 'sday': '2', 'sconent': 'Y', 'sremark': 'Z'},
        ]

        self.mod.save_service_all(data)

        # Two adds for segments plus one for basic
        self.assertGreaterEqual(self.session_mock.add.call_count, 3)
        # Validate objects for segment entries
        added_args = [call.args[0] for call in self.session_mock.add.call_args_list]
        segs = [obj for obj in added_args if obj.__class__.__name__ == 'ServiceBasicSpecialSegmentInfo']
        self.assertEqual(len(segs), 2)
        self.assertEqual(segs[0].kwargs['basic_info_rowguid'], 'U1')
        self.assertEqual(segs[0].kwargs['section_name'], 'A')

    # 4. Should handle application materials and flush after each insert
    def test_application_materials_flush(self):
        data = self.minimal_parsed()
        data['service_application_materials'] = [
            {'unid': 'M1', 'parentUnid': None, 'materialName': 'Form', 'gettypeunids': 1, 'medium': 'req', 'pagenum': '1',
             'necessityIf': 'Y', 'materialsrc': 'src', 'applyAccord': 'acc', 'reportNotice': 'note',
             'materialFormguid': 'f', 'materialFormguidName': 'fn', 'materialExampleguid': 'e',
             'materialExampleguidName': 'en', 'situationTitle': 'first'},
        ]

        self.mod.save_service_all(data)

        # Expect .flush called at least twice (once for basic, once for material)
        self.assertGreaterEqual(self.session_mock.flush.call_count, 2)

    # 5. Should insert related child collections when present
    def test_inserts_multiple_child_collections(self):
        data = self.minimal_parsed()
        data.update({
            'service_market_access': [{
                'name': 'N', 'negativeList_status': 'v', 'xxxx': 's', 'negativeList_itemType': 't',
                'negativeList_industryType': 'i', 'negativeList_name': 'nn', 'negativeList_code': 'nc',
                'measures_name': 'mn', 'measures_code': 'mc', 'localLicensing': 'll', 'scope': 'sc', 'status': 'st',
                'version': 've', 'included': 'Y', 'takeEffectDate': 'ted', 'cancelDate': 'cd', 'measureMatching': 'am'
            }],
            'service_responsibity_author': {
                'stype': 'cat', 'mattercode': 'rc', 'apaservice_name': 'asn', 'deptname': 'dn', 'xslevel': 'xl',
                'according': 'acc', 'remark': 'rk'
            },
            'service_apply': {
                'officeTime': '9-5', 'acceptAddress': 'addr', 'trafficGuide': 'tg', 'applyTerm': 'criteria'
            },
            'service_onlines': [{
                'accept': 'Y', 'dictname': 'online', 'accountTypeName': 'acc', 'towininfo': 'max'
            }],
            'service_processing_procedure': [{
                'name': 'step1', 'step': 'S', 'nodeoperator': 'op', 'limittype': '1d', 'csstandard': 'std', 'transactresult': 'res'
            }],
            'service_handling': {
                'according': 'law'
            },
            'service_asked_question': [{
                'title': 'Q', 'content': 'A'
            }],
            'service_material_verifications': [{
                'materialUnid': 'M1', 'problemUnid': 'P1', 'parentProblemUnid': None, 'problemName': 'What?'
            }]
        })

        self.mod.save_service_all(data)

        # Ensure add called for each collection type at least once
        classes_added = {obj.__class__.__name__ for (obj,) in [c.args for c in self.session_mock.add.call_args_list]}
        expected = {
            'ServiceBasicInformationInfo',
            'ServiceBasicMarknetAccessInfo',
            'ServiceBasicDutyInfo',
            'ServiceCounterServiceInfo',
            'ServiceOnlineProcessingInfo',
            'ServiceProcessingProcedureInfo',
            'ServiceBasisHandlingInfo',
            'ServiceAskedQuestionInfo',
            'ServiceMaterialVerificationInfo',
        }
        self.assertTrue(expected.issubset(classes_added))


if __name__ == '__main__':
    unittest.main(verbosity=2)
