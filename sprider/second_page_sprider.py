"""
请求次级页面 主要获取unid的数据
"""
import requests
import math
from config.seetings import headers, urlConfig, parameter

def fetch_all_services():
    """
    分页获取所有 serviceList 数据
    """
    service_list_all = []

    # 先获取第一页以知道总数
    try:
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

        total = data["total"]
        page_size = 10
        total_pages = math.ceil(total / page_size)

        print(f"共 {total} 条记录，{total_pages} 页")

        # 获取每一页
        for page in range(1, total_pages + 1):
            parameter.get("secondaryPage")['pageNum'] = str(page)
            res = requests.get(
                url=urlConfig.get("secondaryPageUrl"),
                params=parameter.get("secondaryPage"),
                headers=headers,
                timeout=30
            )
            res.raise_for_status()
            message = res.json()

            services = message.get("data", {}).get("serviceList", [])
            service_list_all.extend(services)

        return service_list_all

    except requests.RequestException as e:
        print(f"请求出错: {e}")
        return []
    except Exception as e:
        print(f"解析响应出错: {e}")
        return []


def extract_unids(service_list):
    """
    递归提取所有 unid，无论嵌套层级
    """
    unid_list = []
    def _extract(services):
        if not isinstance(services, list):
            return
        for service in services:
            # 如果有子目录，则递归
            children = service.get("rspApasDirectoryList")
            if children:
                _extract(children)
            else:
                unid = service.get("unid")
                if unid:
                    unid_list.append(unid)

    _extract(service_list)
    return unid_list

