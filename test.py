import requests
from config.seetings import headers

url = 'https://zwfw.fujian.gov.cn:732/cms-business/preview/checkMaterialConfig'

data = {
    "itemUnid": "1760EC5AB6AE7FF685028613C525BECF",
    "materialName": "市政设施建设类审批申请表",
    "materialUnid": "2F2C95174FF97C120AA5F61F59F1382B"
}

data1 = {
    "itemUnid": "C3403F1804931F148C595324F012257E",
    "materialName": "《林草种子生产经营许可证》申请表（种子类、苗木类）",
    "materialUnid": "94E464A1F5C0F33B4B2132BDDD1295F5"
}

res = requests.post(url, json=data1, timeout=30)


# print(res.status_code)
# print(res.text)
#
# exit()
"""
解析页面数据，存放为父子结构 这边是查看的结构
"""

all_node = []

def get_message_children(data):
    childProblems = data.get("childProblems") if data.get("childProblems") else []
    # 获取本身节点id
    problemUnid = data.get("problemUnid")
    # 获取父节点
    parentProblemUnid = data.get("parentProblemUnid")
    # 获取段落文本
    problemName = data.get("problemName")

    for childProblem in childProblems:
        get_message_children(childProblem)

    all_node.append({
        "problemUnid": problemUnid,
        "parentProblemUnid": parentProblemUnid,
        "problemName": problemName,
    })

get_message_children(res.json().get("data"))

print(all_node)