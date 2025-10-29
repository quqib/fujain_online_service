"""
查询数据
"""
from modelsCreate.basic_information_info import BasicInformationInfo
from storage.db import SessionLocal
db = SessionLocal()

def get_missing_in_db(unid_list):
    try:
        # 1. 从数据库查询所有已存在的 rowguid（主键）
        db_rowguids = db.query(BasicInformationInfo.rowguid).all()
        # 转为集合（set），提高查找效率
        db_rowguid_set = {item.rowguid for item in db_rowguids}

        # 3. 找出：在本地列表中，但不在数据库中的 rowguid
        missing_in_db = [guid for guid in unid_list if guid not in db_rowguid_set]

        print("以下 rowguid 在数据库中不存在：")
        print(missing_in_db)

        return missing_in_db

    except Exception as e:
        db.close()
        print("对比检查数据出现报错", e)
