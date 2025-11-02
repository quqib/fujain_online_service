import requests
from config.seetings import headers
from utils.util import get_time_code


url = 'https://zwfw.fujian.gov.cn:732/cms-business/listingDetail/getPowerDetail'
url1 = 'https://zwfw.fujian.gov.cn:732/cms-business/listingDetail/getPowerDetail?powerunid=8BCE85E997CDB50F4B6BC6DEE20129C6&type=1&authId=MTc2MjA2MDI4NC0yMDQ2MjQzNDU2'

url3 = 'https://zwfw.fujian.gov.cn:732/cms-business/apasService/file/downloadFile?unid=0378D0F531625E7DFF185D460D2636EF'
data = {
    "powerunid": "8BCE85E997CDB50F4B6BC6DEE20129C6",
    "type": 1,
    "authId": get_time_code()
}
res = requests.get(url3, headers=headers, timeout=30)
resJson = res.json()
file_url = resJson.get("data")
#下载文件内容（以二进制形式）
file_response = requests.get(file_url, headers=headers, timeout=30)
# 获取二进制内容
binary_content = file_response.content
print(res.status_code)
print(binary_content)


exit()
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