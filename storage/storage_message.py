from db import SessionLocal
from modelsCreate import basic_information_info, special_procedures_info, basis_extablish_info
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
        basicInformation = parsed["basicInformation"]
        # 使用 merge 做 upsert（根据 unique unid），也可先查询再 insert/update
        basic_obj = basic_information_info.BasicInformationInfo(
            unid=basicInformation.get("unid"),
            dir_type=basicInformation.get("dirType"),
            dir_use_level=basicInformation.get("dirUseLevel"),
            dir_anticipateday=basicInformation.get("dirAnticipateday"),
            dir_promiseday=basicInformation.get("dirPromiseday"),
            dept_name=basicInformation.get("deptName"),
            dir_code=basicInformation.get("dirCode"),
            handle_content=basicInformation.get("handleContent"),
            handle_law=basicInformation.get("handleLaw"),
            imgfile=basicInformation.get("imgfile"),
            wordfile=basicInformation.get("wordfile"),
            dir_name=basicInformation.get("dirName"),
            dir_link=basicInformation.get("dirLink"),
        )
        session.add(basic_obj)

        # 特殊环节（如果存在）
        special = parsed.get("special")
        if special:
            special_obj = special_procedures_info.SpecialProceduresInfo(
                basic_unid=basicInformation.get("unid"),
                special_name=special.get("specialName"),
                special_promiseday=special.get("specialPromiseday"),
                special_law=special.get("specialLaw"),
            )
            session.add(special_obj)

        # 依据（可能有多条）
        basisExtablish = parsed.get("basisExtablish", [])
        if basisExtablish:

            for law in basisExtablish:
                law_obj = basisExtablish(
                    basic_unid=basicInformation.get("unid"),
                    law_name=law.get("lawName"),
                    law_symbol=law.get("lawSymbol"),
                    law_implement_dept=law.get("lawImplementdept"),
                    law_implement_date=law.get("lawImplementdate"),
                    law_level_name=law.get("lawLevelName"),
                    law_content=law.get("lawContent"),
                )
                session.add(law_obj)

        # 提交事务（basic+special+laws 要么都成功）
        session.commit()
    except SQLAlchemyError as e:
        # 添加回滚
        session.rollback()
        print("DB 保存失败：", e)
        raise
    finally:
        session.close()
