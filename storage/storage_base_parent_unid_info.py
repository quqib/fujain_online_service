"""
用于存储第一层级中的数据关系
"""
from .db import SessionLocal
from modelsCreate.base_parent_unid_info import BaseParentUnidInfo
from sprider.second_page_sprider import fetch_all_unids


def save_all_unid():
    session = SessionLocal()

    try:
        unid_tuple_list = fetch_all_unids(type=2)
        for unid_tuple in unid_tuple_list:
            unid_obj = BaseParentUnidInfo(
                # 父级节点
                parent_unid=unid_tuple[0],
                # 当前节点
                unid=unid_tuple[1],
                # 部门名称
                dept_name=unid_tuple[2],
                # 词条名称
                commitment_limit=unid_tuple[3],
            )
            session.add(unid_obj)

        session.commit()
    except Exception as e:
        print("存储主关系表数据时出现报错", e)

