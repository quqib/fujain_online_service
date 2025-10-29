from sprider.second_page_sprider import fetch_all_unids
from concurrent.futures import ThreadPoolExecutor, as_completed
from sprider.unid_page_sprider import get_message
from storage.storage_message import save_all
from storage.db import init_db
from config.seetings import unid_list


def main():
    # 初始化数据库
    init_db()
    # 获取列表(unid)
    # unid_list = fetch_all_unids()
    print(unid_list)
    print(len(unid_list))

    # === 关键：找到起始 unid 的索引，然后切片 ===
    start_unid = "F6DAADA0AC9F2F7A046C673CE3A8B1FA"
    start_index = unid_list.index(start_unid)
    print(f"找到起始 unid: {start_unid}，位于列表第 {start_index} 位")

    # 只处理从该位置开始（含）之后的所有 unid
    unids_to_process = unid_list[start_index:]

    # # unid_list = ["unid1", "unid2", "unid3"]  # 测试列表
    # # for unid in unid_list:
    # for unid in unids_to_process:
    #     try:
    #         # if unid != "3BFC9EDE501C069431BA880819C5E49E":
    #         #     continue
    #         # 保存数据
    #         parsed = get_message(unid)
    #         save_all(parsed)
    #         print(f"{unid} 保存成功")
    #     except Exception as e:
    #         print(f"{unid} 处理失败：", e)

    # 定义线程池大小
    max_workers = 10

    def process_single_unid(unid):
        try:
            parsed = get_message(unid)
            save_all(parsed)
            print(f"{unid} 保存成功")
        except Exception as e:
            print(f"{unid} 处理失败：", e)

    # 使用线程池并发执行
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 提交所有任务
        futures = [executor.submit(process_single_unid, unid) for unid in unids_to_process]

        # 可选：等待全部完成（as_completed 可以实时输出结果）
        for future in as_completed(futures):
            pass  # 结果已在 process_single_unid 中打印

if __name__ == "__main__":
    main()


