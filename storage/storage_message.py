from .db import SessionLocal
from modelsCreate.basic_information_info import BasicInformationInfo
from modelsCreate.basic_information_picture_info import BasicInformationPictureInfo
from modelsCreate.special_procedures_info import SpecialProceduresInfo
from modelsCreate.basis_extablish_info import BasisEstablishInfo
from modelsCreate.application_material_info import ApplicationMaterialInfo

from sqlalchemy.exc import SQLAlchemyError

def save_all(parsed: dict):
    """
    parsed: {
        "applicationMaterial": { ... },
        "specialProcedures": {...} or None,
        "basisExtablish": [ {...}, {...} ]
    }
    """
    session = SessionLocal()
    try:
        basic = parsed["basic"]
        # 使用 merge 做 upsert（根据 unique unid），也可先查询再 insert/update
        basic_obj = BasicInformationInfo(
            # 主键
            rowguid=basic.get("unid"),

            # 基本信息
            item_type=basic.get("dirType"),
            exercise_level=basic.get("dirUseLevel"),
            legal_limit=basic.get("dirAnticipateday"),
            commitment_limit=basic.get("dirPromiseday"),
            department_name=basic.get("deptName"),
            item_code=basic.get("dirCode"),

            # 是否收费
            is_charging=basic.get("chargeFlag"),
            # 收费类型
            charge_items=basic.get("chargeItems"),
            # 办理条件
            handling_conditions=basic.get("handleContent"),
            handling_basis=basic.get("handleLaw"),

            # 项目名称
            dir_name=basic.get("dirName"),
            # 项目链接
            dir_link=basic.get("dirLink"),
        )
        session.add(basic_obj)
        session.commit()

        # 存储二进制图片 二进制docx文件
        basic_picture = parsed.get("basic_picture", {})
        if basic_picture:
            for key, value in basic_picture.items():
                basic_picture_obj = BasicInformationPictureInfo(
                    basic_info_rowguid=basic.get("unid"),
                    approval_result_material_name=key,
                    approval_result_material=value
                )
                session.add(basic_picture_obj)

        # 特殊环节（如果存在）
        special = parsed.get("special")
        if special:
            special_obj = SpecialProceduresInfo(
                basic_info_rowguid=basic.get("unid"),
                special_link_name=special.get("specialName"),
                commitment_limit=special.get("specialPromiseday"),
                basis_of_establishment=special.get("specialLaw"),
            )
            session.add(special_obj)

        # 设立依据(可能有多条)
        laws = parsed.get("laws", [])
        if laws:
            for law in laws:
                law_obj = BasisEstablishInfo(
                    basic_info_rowguid=basic.get("unid"),
                    # 依据文件名称
                    basis_file_name=law.get("lawName"),
                    # 依据文号
                    basis_doc_number=law.get("lawSymbol"),
                    # 颁布机关
                    issuing_authority=law.get("lawImplementdept"),
                    # 实施日期
                    effective_date=law.get("lawImplementdate"),
                    # 依据级别
                    basis_level=law.get("lawLevelName"),
                    # 条款内容
                    clause_content=law.get("lawContent"),
                )
                session.add(law_obj)

        # 获取申报材料(可能多条)
        application_materials = parsed.get("application_materials", [])
        if application_materials:
            for application_material in application_materials:
                application_material_obj = ApplicationMaterialInfo(
                    # 外键
                    basic_info_rowguid=basic.get("unid"),
                    # 文件类型
                    file_type=application_material.get("materialName"),
                    # 材料本身unid
                    material_unid = application_material.get("unid"),
                    # 父节点
                    parent_unid=application_material.get("parentUnid"),
                    # 材料形式(1-纸质，电子材料 3-纸质 7-电子材料)
                    material_form=application_material.get("materialOrdernum"),
                    # 材料要求
                    material_requirements=application_material.get("materialMedium"),
                    # 份数
                    material_pagenum = application_material.get("materialPagenum"),
                    # 材料必要性
                    material_necessity=application_material.get("materialIsneed"),
                    # 来源渠道
                    source_channel=application_material.get("materialSourcechannelName"),
                    # 具体要求
                    specific_requirements=application_material.get("materialPageformat"),
                    # 设立依据
                    basis_of_establishment=application_material.get("materialLaw"),
                    # 材料核查标准
                    material_check_standard=application_material.get("material_check_standard"),
                    # 附件下载
                    # 格式文本
                    material_formguid=application_material.get("materialFormguid"),
                    # 名称
                    material_formguid_name=application_material.get("materialFormguName"),
                    # 示范文本
                    material_exampleguid=application_material.get("materialExampleguid"),
                    # 名称
                    material_exampleguid_name=application_material.get("materialExampleguName"),

                    # 首次申请（是否为首次申请）
                    first_application=application_material.get("situationTitle"),
                )
                session.add(application_material_obj)

        # 提交事务（basic+special+laws 要么都成功）
        session.commit()
    except SQLAlchemyError as e:
        # 添加回滚
        session.rollback()
        print("DB 保存失败：", e)
        raise
    finally:
        session.close()
