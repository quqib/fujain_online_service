"""
获取第一层页面的底部链接
"""

import random
import time

import requests
from config.seetings import headers, urlConfig, parameter


# 获取页面底部链接
def get_middle_unid(unid):
    params = parameter["getBottomLink"].copy()
    params["unid"] = unid

    res_basic = requests.get(
        url=urlConfig.get("getBottomLinkUrl"),
        params=params,
        headers=headers,
        timeout=30
    )
    data_basic = res_basic.json().get("data", {})[0]

    serviceUnid = data_basic.get("serviceUnid", "") if data_basic else ""

    return serviceUnid



