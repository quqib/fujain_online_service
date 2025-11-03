import random
import time

import requests
import math
from config.seetings import headers, urlConfig, parameter

def fetch_all_unids(type=1):
    """
    分页获取所有 serviceList 并直接提取 unid
    """
    unid_list = []

    try:
        # 获取第一页
        res = requests.get(
            url=urlConfig.get("secondaryPageUrl"),
            params=parameter.get("secondaryPage"),
            headers=headers,
            timeout=30
        )
        res.raise_for_status()
        data = res.json().get("data")
        if not data:
            print("API 返回无数据")
            return []

        total = res.json().get("total")
        page_size = 10
        total_pages = math.ceil(int(total) / page_size)

        print(f"共 {total} 条记录，{total_pages} 页")

        # 遍历每页
        for page in range(1, total_pages + 1):
            # if page == 2:
            #     break
            print(f"运行至{page}页")
            time.sleep(random.randint(5, 10))
            parameter.get("secondaryPage")['pageNum'] = str(page)
            res = requests.get(
                url=urlConfig.get("secondaryPageUrl"),
                params=parameter.get("secondaryPage"),
                headers=headers,
                timeout=30
            )
            res.raise_for_status()
            service_list = res.json().get("data", {}).get("serviceList", [])
            if type == 1:
                # 递归提取 unid
                _extract_unids(service_list, unid_list)

            else:
                _extract_unid_tuples(service_list, unid_list)

        return unid_list

    except requests.RequestException as e:
        print(f"请求出错: {e}")
        return []
    except Exception as e:
        print(f"解析响应出错: {e}")
        return []

# 这里返回的是最后一个有效的unid
def _extract_unids(services, unid_list):
    """
    递归提取 unid，内部使用
    """
    if not isinstance(services, list):
        return
    for service in services:
        children = service.get("rspApasDirectoryList")
        if children:
            _extract_unids(children, unid_list)
        else:
            unid = service.get("unid")
            if unid:
                unid_list.append(unid)

# 这里返回的是层级结构
def _extract_unid_tuples(services, result_tuples):
    """
    递归提取每个节点的 (parent_unid, unid) 元组
    :param services: 当前层级的服务列表（可能是 list 或 dict）
    :param result_tuples: 存放结果的列表，元素为 (parent_unid, unid)
    """
    # 如果是字典，转成单元素列表处理
    if isinstance(services, dict):
        services = [services]

    if not isinstance(services, list):
        return

    for service in services:
        unid = service.get("unid")
        parent_unid = service.get("parentUnid")  # 注意字段名是 parentUnid（驼峰）

        # 获取部门名称
        dept_name = service.get("deptName")
        dir_name = service.get("dirName")


        # 只要当前节点有 unid，就记录 (parent_unid, unid)
        if unid:
            result_tuples.append((parent_unid, unid, dept_name, dir_name))

        # 递归处理子节点
        children = service.get("rspApasDirectoryList")
        if children:
            _extract_unid_tuples(children, result_tuples)
