from config.seetings import unid_list_all, unid_list_seeting, unid_list_check

# 对比两个列表取出不同的文件
def get_missing_in_list(unid_list, db_rowguid_set):
    try:
        # 3. 找出：在本地列表中，但不在数据库中的 rowguid
        missing_in_db = [guid for guid in unid_list if guid not in db_rowguid_set]

        print("以下 rowguid 在数据库中不存在：")
        print(missing_in_db)

        return missing_in_db

    except Exception as e:
        print("对比检查数据出现报错,utils文件函数", e)
