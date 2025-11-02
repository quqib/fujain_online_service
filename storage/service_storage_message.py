from .db import SessionLocal
from modelsCreate.modelsService.service_basic_information_info import ServiceBasicInformationInfo
from modelsCreate.modelsService.service_basic_marknet_access_info import ServiceBasicMarknetAccessInfo
from modelsCreate.modelsService.service_basic_special_segment_info import ServiceBasicSpecialSegmentInfo
from modelsCreate.modelsService.service_basic_duty_info import ServiceBasicDutyInfo
from modelsCreate.modelsService.service_counter_service_info import ServiceCounterServiceInfo
from modelsCreate.modelsService.service_online_processing_info import ServiceOnlineProcessingInfo
from modelsCreate.modelsService.service_processing_procedure_info import ServiceProcessingProcedureInfo
from modelsCreate.modelsService.service_asked_question_info import ServiceAskedQuestionInfo
from modelsCreate.modelsService.service_basis_handling_info import ServiceBasisHandlingInfo
from modelsCreate.modelsService.service_application_material_info import ServiceApplicationMaterialInfo
from modelsCreate.modelsService.service_material_verification_info import ServiceMaterialVerificationInfo

from sqlalchemy.exc import SQLAlchemyError

def save_service_all(parsed: dict):
    """
    parsed: {
        "applicationMaterial": { ... },
        "specialProcedures": {...} or None,
        "basisExtablish": [ {...}, {...} ]
    }
    """
    session = SessionLocal()
    try:
        service_basic = parsed["service_basic"]
        # 使用 merge 做 upsert（根据 unique unid），也可先查询再 insert/update
        service_basic_obj = ServiceBasicInformationInfo(
            # 主键
            rowguid=service_basic.get("unid"),
            # 外键
            basic_info_rowguid = service_basic.get("basic_info_rowguid"),

            # 事项编码
            item_code=service_basic.get("infoprojid"),
            # 基本编码
            basic_code=service_basic.get("baseCode"),
            # 实施编码
            implement_code=service_basic.get("implCode"),
            # 业务办理项编码
            business_item_code=service_basic.get("taskHandleItem"),


            # 办件类型
            handling_type=service_basic.get("servicetype"),
            # 事项类型
            item_type=service_basic.get("addTypeName"),
            # 行使层级
            exercise_level=service_basic.get("performLevelName"),
            # 法定时限
            legal_limit=service_basic.get("lawlimit"),
            # 承诺时限
            commitment_limit=service_basic.get("promiseday"),
            # 承诺时限说明
            commitment_limit_explan=service_basic.get("promisdayinfo"),


            # 实施主体
            implementation_body=service_basic.get("deptname"),
            # 实施主体性质
            body_nature=service_basic.get("deptPropertyName"),
            # 委托部门
            entrusted_department=service_basic.get("deptEntrust"),
            # 联办机构
            joint_agencies=service_basic.get("coopOrg"),
            # 主办处室
            host_office=service_basic.get("leadDept"),

            # 权力来源
            power_source=service_basic.get("rightSourceName"),
            # 联系电话
            contact_phone=service_basic.get("contactphone"),
            # 监督投诉电话
            supervision_phone=service_basic.get("monitorcomplain"),
            # 一件事集成套餐(这个是一个链接)
            # 中介服务
            intermediary_services=service_basic.get("intermediaryServicesList"),

            # 审批结果名称
            approval_result_name=service_basic.get("resultName"),
            # 审批结果类型
            approval_result_type=service_basic.get("finishTypeName"),
            # 审批结果样本
            approval_result_sample=service_basic.get("resultFileType"),
            # 审批结果样本名称
            approval_result_sample_name=service_basic.get("resultFileName"),
            # 审批结果样本类型
            approval_result_sample_type=service_basic.get("resultFileType"),
            # 审批结果共享
            approval_result_share=service_basic.get("finishType"),
            # 结果领取方式
            result_receive_method=service_basic.get("finishGetTypeName"),
            # 结果领取说明
            result_receive_desc=service_basic.get("finishInfo"),

            # 申报对象
            applicant_type=service_basic.get("userType"),

            # 是否进驻政务大厅
            in_service_hall=service_basic.get("enterif"),
            # 办理形式
            handling_form=service_basic.get("handleForm"),
            # 必须现场办理原因
            must_on_site_reason=service_basic.get("sceneReason"),

            # 企业办事主题
            enterprise_theme=service_basic.get("qiyeTheme"),
            # 网上办理深度
            online_depth=service_basic.get("webApplyDegreeName"),

            # 通办范围
            nationwide_coverage=service_basic.get("nearbyAreaName"),
            # 数量限制
            quantity_limit=service_basic.get("countLimit"),
            # 通办范围说明
            coverage_description=service_basic.get("nearbyInstruction"),

            # 是否全国高频“跨省通办”事项
            is_national_cross_province=service_basic.get("highFrequencyKstb"),
            # 跨省通办模式（将网上办理深度括号外的提取出来）
            cross_province_mode=service_basic.get("webApplyDegreeName"),
            # 跨省通办模式说明
            cross_province_explain=service_basic.get("kstbModel"),
            # 跨省代收代办区域
            cross_province_areas=service_basic.get("kstbOutAreaname"),

            # 计划生效日期
            planned_effective_date=service_basic.get("planEnableDate"),
            # 计划取消日期
            planned_cancel_date=service_basic.get("planCancelDate"),

            # 是否开通预约服务
            has_reservation=service_basic.get("isSubscribeService"),
            # 是否支持自助终端办理
            support_self_service_terminal=service_basic.get("terminalSupport"),
            # 面向自然人地方特色主题分类
            individual_theme_category=service_basic.get("personalThemeCategory"),
            # 面向法人地方特色主题分类
            corporate_theme_category=service_basic.get("companyThemeCategory"),

            # 移动端是否对接单点登录
            mobile_sso_enabled=service_basic.get("mobileSingleLogin"),
            # 计算机端是否对接单点登录
            pc_sso_enabled=service_basic.get("pcSingleLogin"),

            # 乡镇街道名称
            town_street_name=service_basic.get("smallTownsName"),
            # 乡镇街道代码
            town_street_code=service_basic.get("smallTownsCode"),
            # 村镇社区名称
            village_community_name=service_basic.get("communityName"),
            # 村镇社区代码
            village_community_code=service_basic.get("communityCode"),

            # 是否支持物流快递
            support_logistics=service_basic.get("logisticsExpress"),
            # 是否支持网上支付
            support_online_payment=service_basic.get("onlinePay"),

            # 事项状态
            status=service_basic.get("state"),
            # 是否全程代办 N代表否 Y代表是
            full_proxy_enabled=service_basic.get("agentFlag"),

            # 是否收费
            charge_limit=service_basic.get("chargeLimit"),

            # 备注
            remarks=service_basic.get("iremark"),

            # 项目链接
            dir_link=service_basic.get("dirLink"),

        )
        session.add(service_basic_obj)
        session.commit()

        # 存储特殊环节-使用for循环写入
        service_section_list = parsed.get("service_section_list", [])
        if service_section_list:
            for service_section in service_section_list:
                service_section_obj = ServiceBasicSpecialSegmentInfo(
                    # 外键
                    basic_info_rowguid=service_basic.get("unid"),
                    # 特殊环节名称
                    section_name=service_section.get("sname"),
                    # 特殊环节时限
                    section_time_limit=service_section.get("sday"),
                    # 特殊环节依据
                    Section_basis=service_section.get("sconent"),
                    # 特殊环节备注
                    Section_remark=service_section.get("sremark"),
                )
                session.add(service_section_obj)


        # 存储市场准入负面清单许可准入措施列表使用for循环进行写入
        service_market_access = parsed.get("service_market_access", [])
        if service_market_access:
            for service_market_acces in service_market_access:
                service_market_acces_obj = ServiceBasicMarknetAccessInfo(
                    # 外键
                    basic_info_rowguid=service_basic.get("unid"),
                    # 名称
                    market_name=service_market_acces.get("name"),
                    # 负面清单版本
                    market_negativate_version=service_market_acces.get("negativeList_status"),
                    # 负面清单事项状态
                    market_negativate_status=service_market_acces.get("xxxx"),
                    # 负面清单类别
                    market_negativate_type=service_market_acces.get("negativeList_itemType"),
                    # 行业
                    market_negativate_industry=service_market_acces.get("negativeList_industryType"),
                    # 负面清单事项名称
                    market_negativate_name=service_market_acces.get("negativeList_name"),
                    # 负面清单事项编码
                    market_negativate_code=service_market_acces.get("negativeList_code"),

                    # 负面清单事项措施名称
                    market_negativate_measure_name=service_market_acces.get("measures_name"),
                    # 负面清单事项措施编码
                    market_negativate_measure_code=service_market_acces.get("measures_code"),
                    # 地方性许可措施
                    local_license_measure=service_market_acces.get("localLicensing"),
                    # 适用范围
                    applicable_scope=service_market_acces.get("scope"),
                    # 事项措施状态
                    market_negativate_measure_status=service_market_acces.get("status"),
                    # 负面清单事项措施版本
                    market_negativate_measure_version=service_market_acces.get("version"),
                    # 是否暂时列入清单
                    is_temporarily_included=service_market_acces.get("included"),
                    # 计划生效日期
                    planned_effective_date=service_market_acces.get("takeEffectDate"),
                    # 计划取消日期
                    planned_cancel_date=service_market_acces.get("cancelDate"),

                    # 关联的政务服务事项基本目录
                    associated_service_item=service_market_acces.get("measureMatching"),
                )
                session.add(service_market_acces_obj)

        # 存储权责清单
        service_responsibity_author = parsed.get("service_responsibity_author")
        if service_responsibity_author:
            service_responsibity_author_obj = ServiceBasicDutyInfo(
                # 外键
                basic_info_rowguid=service_basic.get("unid"),
                # 类别
                category=service_responsibity_author.get("stype"),
                # 权责编码
                responsibility_code=service_responsibity_author.get("mattercode"),
                # 关联服务事项名称
                associated_service_item_name=service_responsibity_author.get("apaservice_name"),
                # 行使主体（实施该权力的部门名称）
                exercising_body=service_responsibity_author.get("deptname"),
                # 行使层级（如“国家级”、“省级”、“市级”、“县级”、“乡级”）
                exercise_level=service_responsibity_author.get("xslevel"),
                # 实施依据
                implementation_basis=service_responsibity_author.get("according"),
                # 备注
                remarks=service_responsibity_author.get("remark"),
            )
            session.add(service_responsibity_author_obj)

        # 存储申报材料
        service_application_materials = parsed.get("service_application_materials", [])
        if service_application_materials:
            for service_application_material in service_application_materials:
                service_application_material_obj = ServiceApplicationMaterialInfo(
                    # 外键
                    basic_info_rowguid=service_basic.get("unid"),
                    # 申报材料unid
                    material_unid=service_application_material.get("unid"),
                    # 父节点
                    parent_unid=service_application_material.get("parentUnid"),
                    # 文件类型
                    file_type=service_application_material.get("materialName"),
                    # 材料形式(1-纸质，电子材料 3-纸质 7-电子材料)
                    material_form=service_application_material.get("gettypeunids"),
                    # 材料要求
                    material_requirements=service_application_material.get("medium"),
                    # 份数
                    material_pagenum=service_application_material.get("pagenum"),
                    # 材料必要性
                    material_necessity=service_application_material.get("necessityIf"),
                    # 来源渠道
                    source_channel=service_application_material.get("materialsrc"),
                    # 设立依据
                    basis_of_establishment=service_application_material.get("applyAccord"),
                    # 填报须知
                    filling_instructions=service_application_material.get("reportNotice"),
                    # 附件下载
                    # 格式文本
                    material_formguid=service_application_material.get("materialFormguid"),
                    # 格式文本名称
                    material_formguid_name=service_application_material.get("materialFormguidName"),
                    # 示范文本
                    material_exampleguid=service_application_material.get("materialExampleguid"),
                    # 示范文本名称
                    material_exampleguid_name=service_application_material.get("materialExampleguidName"),
                    # 首次申请（是否为首次申请）
                    first_application=service_application_material.get("situationTitle"),
                )
                session.add(service_application_material_obj)

        # 材料核查
        service_material_verifications = parsed.get("service_material_verifications", [])
        if service_material_verifications:
            for service_material_verification in service_material_verifications:
                service_material_verification_obj = ServiceMaterialVerificationInfo(
                    # 外键
                    basic_info_rowguid=service_material_verification.get("materialUnid"),
                    # 本身节点
                    problem_unid=service_material_verification.get("problemUnid"),
                    # 父级节点
                    parent_problem_unid=service_material_verification.get("parentProblemUnid"),
                    # 本身字段
                    problem_name=service_material_verification.get("problemName"),
                )
                session.add(service_material_verification_obj)


        # 存储窗口办理+受理条件
        service_apply = parsed.get("service_apply")
        if service_apply:
            service_apply_obj = ServiceCounterServiceInfo(
                # 外键
                basic_info_rowguid=service_basic.get("unid"),
                # 办理时间
                handling_time=service_apply.get("officeTime"),
                # 办理地点
                service_location=service_apply.get("acceptAddress"),
                # 交通指引
                transportation_guide=service_apply.get("trafficGuide"),
                # 受理条件
                acceptance_criteria=service_apply.get("applyTerm"),
            )
            session.add(service_apply_obj)

        # 网上办理
        service_onlines = parsed.get("service_onlines", [])
        if service_onlines:
            for service_online in service_onlines:
                service_online_obj = ServiceOnlineProcessingInfo(
                    # 外键
                    basic_info_rowguid=service_basic.get("unid"),
                    # 是否涉及
                    does_it_involve=service_online.get("accept"),
                    # 网上申请方式
                    online_application_method=service_online.get("dictname"),
                    # 账户要求
                    account_requirements=service_online.get("accountTypeName"),
                    # 承诺到窗口最多次数说明
                    max_visit_commitment=service_online.get("towininfo"),
                )
                session.add(service_online_obj)

        # 办理流程
        service_processing_procedures = parsed.get("service_processing_procedure", [])
        if service_processing_procedures:
            for service_processing_procedure in service_processing_procedures:
                service_processing_procedure_obj = ServiceProcessingProcedureInfo(
                    # 外键
                    basic_info_rowguid=service_basic.get("unid"),
                    # 办理流程
                    procedure_name=service_processing_procedure.get("name"),
                    # 步骤类型
                    step_type=service_processing_procedure.get("step"),
                    # 办理人
                    handler=service_processing_procedure.get("nodeoperator"),
                    # 办理时限
                    handling_time_limit = service_processing_procedure.get("limittype"),
                    # 审查标准
                    review_criteria=service_processing_procedure.get("csstandard"),
                    # 办理结果
                    handling_result=service_processing_procedure.get("transactresult"),
                )
                session.add(service_processing_procedure_obj)

        # 办理依据
        service_handling = parsed.get("service_handling")
        if service_handling:
            service_handling_obj = ServiceBasisHandlingInfo(
                # 外键
                basic_info_rowguid=service_basic.get("unid"),
                # 办理依据
                basis_handling=service_handling.get("according"),
            )
            session.add(service_handling_obj)

        # 常见问题
        service_asked_questions = parsed.get("service_asked_question", [])
        if service_asked_questions:
            for service_asked_question in service_asked_questions:
                service_asked_question_obj = ServiceAskedQuestionInfo(
                    # 外键
                    basic_info_rowguid=service_basic.get("unid"),
                    # 问题名称
                    question_name=service_asked_question.get("title"),
                    # 问题内容
                    question_content=service_asked_question.get("content"),
                )
                session.add(service_asked_question_obj)


        # 提交事务（basic+special+laws 要么都成功）
        session.commit()
    except SQLAlchemyError as e:
        # 添加回滚
        session.rollback()
        print("DB 保存失败：", e)
        raise
    finally:
        session.close()
