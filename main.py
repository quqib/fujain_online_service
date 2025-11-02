import threading
import queue
from concurrent.futures import ThreadPoolExecutor, as_completed
from sprider.second_page_sprider import fetch_all_unids
from sprider.get_middle_unid import get_middle_unid
from sprider.unid_page_sprider import get_message
from storage.storage_message import save_all
from sprider.service_unid_page_sprider import service_get_message
from storage.service_storage_message import save_service_all
from storage.db import init_db

def main():
    init_db()
    # 获取所有的unid
    unid_list = fetch_all_unids()

    # unid_list = ["E9D22FD97F359D97144DC46A160EA7A5"]
    # 池大小（可按需调整）
    producer_workers = 10  # 用于处理 unid（第一阶段）
    consumer_workers = 6   # 用于处理 service_unid（第二阶段）
    queue_maxsize = 0      # 0 或 None 表示无限制；可设置限制以做背压

    # 线程安全队列：生产者把 service_unid 放入，消费者取出处理
    svc_queue = queue.Queue(maxsize=queue_maxsize)

    # 如果你想记录哪些 unid 已成功处理（可选）
    successful_unids = []
    success_lock = threading.Lock()

    # 生产者：处理 unid，保存 unid 数据，并把 service_unid 放入队列
    def producer_task(unid):
        try:
            parsed = get_message(unid)   # 处理并返回解析数据
            save_all(parsed)             # 保存 unid 二层数据（先保存）
            print(f"{unid} 二层保存成功")

            # 立即尝试获取对应的 service_unid（可能为空字符串）
            try:
                service_unid = get_middle_unid(unid)
            except Exception as e_inner:
                print(f"{unid} 获取 service_unid 失败：{e_inner}")
                service_unid = ""

            # 如果拿到了有效 service_unid，就投递到队列（由消费者并发处理）
            if service_unid:
                svc_queue.put((unid, service_unid))  # 也可以只放 service_unid，根据需要
                print(f"{unid} -> service_unid 已入队：{service_unid}")
            else:
                print(f"{unid} 未获取到有效 service_unid")

            # 可选：记录成功的 unid（或用于统计/后续处理）
            with success_lock:
                successful_unids.append(unid)

        except Exception as e:
            print(f"{unid} 二层处理失败：", e)

    # 消费者：从队列取 service_unid 并保存（或进一步爬取）
    def consumer_task():
        while True:
            item = svc_queue.get()
            if item is None:
                # 收到终止信号，退出循环
                svc_queue.task_done()
                break

            unid, service_unid = item
            try:
                # 这里 save_service_all 应该是根据 service_unid 获取并保存三层数据
                parsed_service = service_get_message(service_unid, unid)
                save_service_all(parsed_service)
                print(f"{unid}（三层）{service_unid} 保存成功")
            except Exception as e:
                print(f"{unid}（三层）{service_unid} 处理失败：", e)
            finally:
                svc_queue.task_done()

    # 启动消费者线程（使用 ThreadPoolExecutor 或直接 threading.Thread）
    consumer_threads = []
    for _ in range(consumer_workers):
        t = threading.Thread(target=consumer_task, daemon=True)
        t.start()
        consumer_threads.append(t)

    # 使用线程池并发运行生产者任务（处理 unid）
    with ThreadPoolExecutor(max_workers=producer_workers) as prod_executor:
        futures = [prod_executor.submit(producer_task, unid) for unid in unid_list]
        # 可以使用 as_completed 来打印或监控进度
        for f in as_completed(futures):
            # 如果需要，可以检查 f.result() 或捕获异常（producer_task 内部已捕获）
            pass

    # 等待所有已经放入队列的 item 被处理完
    svc_queue.join()  # 阻塞直到队列中的所有任务都被 task_done

    # 通知消费者线程退出：为每个消费者放一个 None 哨兵
    for _ in range(consumer_workers):
        svc_queue.put(None)

    # 等待消费者线程结束（可选）
    for t in consumer_threads:
        t.join()

    print("所有任务完成")
    print(f"成功处理的 unid 数量: {len(successful_unids)}")

if __name__ == "__main__":
    main()
