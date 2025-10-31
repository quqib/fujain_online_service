import requests

url = 'https://zwfw.fujian.gov.cn:732/cms-business/preview/checkMaterialConfig'

data = {
    "itemUnid": "1760EC5AB6AE7FF685028613C525BECF",
    "materialName": "市政设施建设类审批申请表",
    "materialUnid": "2F2C95174FF97C120AA5F61F59F1382B"
}

res = requests.post(url, json=data, timeout=30)
print(res.status_code)
print(res.text)

"""
解析页面数据，存放为父子结构
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





