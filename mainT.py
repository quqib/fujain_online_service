import time
import requests
from typing import List
from sprider.second_page_sprider import fetch_all_unids
from sprider.unid_page_sprider import get_message
from storage.storage_message import save_all
from storage.db import init_db


# 网络检测函数：检测是否能访问一个稳定的公网地址
def is_network_ok(url="http://www.baidu.com", timeout=5) -> bool:
    try:
        requests.head(url, timeout=timeout, allow_redirects=True)
        return True
    except Exception:
        return False


# 等待网络恢复
def wait_for_network(max_wait_time=300, check_interval=10):
    print("检测到网络不可用，正在等待恢复...")
    elapsed = 0
    while elapsed < max_wait_time:
        if is_network_ok():
            print("网络已恢复！")
            return True
        print(f"等待 {check_interval} 秒后重试...")
        time.sleep(check_interval)
        elapsed += check_interval
    print("等待超时，网络仍未恢复。")
    return False


# 带重试的单个 unid 处理
def process_unid_with_retry(unid: str, max_retries=3, retry_delay=2):
    for attempt in range(max_retries + 1):
        try:
            # 尝试获取数据
            parsed = get_message(unid)
            if parsed:  # 假设返回非空表示成功
                save_all(parsed)
                print(f"{unid} 保存成功")
                return True  # 成功返回
            else:
                print(f"{unid} 返回空数据，可能是临时问题")
        except Exception as e:
            print(f"第 {attempt + 1} 次尝试失败: {unid} -> {e}")

        # 如果是最后一次尝试，不再重试
        if attempt == max_retries:
            print(f"{unid} 达到最大重试次数，处理失败。")
            return False

        # 检查网络
        if not is_network_ok():
            print(f"{unid}: 网络异常，等待恢复...")
            if not wait_for_network():
                print(f"{unid}: 网络恢复失败，跳过该 unid。")
                return False

        # 等待一段时间后重试
        time.sleep(retry_delay)

def main():
    # 初始化数据库
    init_db()

    # 获取所有 unid
    unid_list = fetch_all_unids()
    print(f"共获取到 {len(unid_list)} 个 unid")

    # 可选：记录已处理的 unid，防止重复处理（建议写入文件或数据库）
    processed_file = "processed_unids.txt"
    processed_unids = set()

    # 读取已处理的 unid（断点续传）
    try:
        with open(processed_file, "r", encoding="utf-8") as f:
            processed_unids = set(line.strip() for line in f if line.strip())
    except FileNotFoundError:
        pass

    print(f"已处理 {len(processed_unids)} 个 unid（断点续传）")

    for unid in unid_list:
        if unid in processed_unids:
            print(f"{unid} 已处理，跳过...")
            continue

        success = process_unid_with_retry(unid, max_retries=3)

        # 记录处理状态
        with open(processed_file, "a", encoding="utf-8") as f:
            f.write(unid + "\n")

        if success:
            processed_unids.add(unid)
        else:
            print(f"{unid} 处理失败，已记录，下次可单独排查")

if __name__ == "__main__":
    main()
