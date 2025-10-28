from sprider.second_page_sprider import fetch_all_unids
from sprider.unid_page_sprider import get_message
from storage.storage_message import save_all
from storage.db import init_db


def main():
    # 初始化数据库
    init_db()
    # 获取列表(unid)
    unid_list = fetch_all_unids()
    print(unid_list)
    print(len(unid_list))
    # unid_list = ["unid1", "unid2", "unid3"]  # 测试列表
    for unid in unid_list:
        try:
            # if unid != "3BFC9EDE501C069431BA880819C5E49E":
            #     continue
            # 保存数据
            parsed = get_message(unid)
            save_all(parsed)
            print(f"{unid} 保存成功")
        except Exception as e:
            print(f"{unid} 处理失败：", e)

if __name__ == "__main__":
    main()


