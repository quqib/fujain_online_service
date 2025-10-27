# storage.py
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
        basic = parsed["basic"]
        # 使用 merge 做 upsert（根据 unique unid），也可先查询再 insert/update
        basic_obj = basic_information_info.ApplicationMaterialInfo(
            unid=basic.get("unid"),
            dir_type=basic.get("dirType"),
            dir_use_level=basic.get("dirUseLevel"),
            dir_anticipateday=basic.get("dirAnticipateday"),
            dir_promiseday=basic.get("dirPromiseday"),
            dept_name=basic.get("deptName"),
            dir_code=basic.get("dirCode"),
            handle_content=basic.get("handleContent"),
            handle_law=basic.get("handleLaw"),
            imgfile=basic.get("imgfile"),
            wordfile=basic.get("wordfile"),
            dir_name=basic.get("dirName"),
            dir_link=basic.get("dirLink"),
        )
        # 如果想更新已存在记录，用 merge
        session.merge(basic_obj)

        # 特殊环节（如果存在）
        special = parsed.get("special")
        if special:
            special_obj = special_procedures_info.SpecialProceduresInfo(
                basic_unid=basic.get("unid"),
                special_name=special.get("specialName"),
                special_promiseday=special.get("specialPromiseday"),
                special_law=special.get("specialLaw"),
            )
            session.add(special_obj)

        # 依据（可能有多条），先删除旧的 law 然后插入新的（根据业务决定）
        basisExtablish = parsed.get("basisExtablish", [])
        if basisExtablish:
            # 选项：先删除旧的 law（简单做法）
            session.query(basisExtablish).filter(basisExtablish.basic_unid == basic.get("unid")).delete()

            for law in laws:
                law_obj = Law(
                    basic_unid=basic.get("unid"),
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
