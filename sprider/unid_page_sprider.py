"""
获取三级页面的页面信息 按照要求不包括页脚的跳转链接内的信息
"""
import random
import time

import requests
from config.seetings import headers, urlConfig, parameter


def get_message(unid):
    # -------------------------------
    # 1️.获取基础信息
    # -------------------------------
    params = parameter["basicInformation"].copy()
    params["unid"] = unid

    res_basic = requests.get(
        url=urlConfig.get("basicInformationUrl"),
        params=params,
        headers=headers,
        timeout=30
    )
    data_basic = res_basic.json().get("data", {})

    apasDirectory = data_basic.get("apasDirectory", {})
    basic = {
        "unid": apasDirectory.get("unid"),
        # 事项类型
        "dirType": apasDirectory.get("dirType"),
        # 行使层级
        "dirUseLevel": apasDirectory.get("dirUseLevel"),
        # 法定时限
        "dirAnticipateday": apasDirectory.get("dirAnticipateday"),
        # 承诺时限
        "dirPromiseday": apasDirectory.get("dirPromiseday"),
        # 部门名称
        "deptName": apasDirectory.get("deptName"),
        # 事项编码
        "dirCode": apasDirectory.get("dirCode"),
        # 办理条件
        "handleContent": apasDirectory.get("handleContent"),
        # 办理条件设立依据
        "handleLaw": apasDirectory.get("handleLaw"),
        # 是否收费 1-收费 0-不收费
        "chargeFlag": apasDirectory.get("chargeFlag"),
        # 收费类型
        "chargeItems": apasDirectory.get("chargeItems"),
        # 名称
        "dirName": apasDirectory.get("dirName"),
        # 链接
        "dirLink": f"https://zwfw.fujian.gov.cn/standartCatalogGuide?unid={apasDirectory.get('unid')}"
    }
    # 审批材料
    imgfile = data_basic.get("imgfile", [])
    wordfile = data_basic.get("wordfile", []),

    # 存放基础信息中的图片和文本
    # 办理流程图
    basic_picture = deal_basic_picture(imgfile, wordfile)

    # -------------------------------
    # 2️.特殊环节
    # -------------------------------
    specialList = data_basic.get("specialList") or []
    special = {}
    if specialList:
        specialItem = specialList[0]
        special = {
            # 特殊环节名称
            "specialName": specialItem.get("specialName"),
            # 承诺时限
            "specialPromiseday": specialItem.get("specialPromiseday"),
            # 设立依据
            "specialLaw": specialItem.get("specialLaw")
        }

    # -------------------------------
    # 2️.设立依据
    # -------------------------------
    lawList = data_basic.get("lawList") or []
    laws = []
    for law in lawList:
        laws.append({
            # 依据文件名称
            "lawName": law.get("lawName"),
            # 依据文号
            "lawSymbol": law.get("lawSymbol"),
            # 颁布机关
            "lawImplementdept": law.get("lawImplementdept"),
            # 实施日期
            "lawImplementdate": law.get("lawImplementdate"),
            # 依据级别
            "lawLevelName": law.get("lawLevelName"),
            # 条款内容
            "lawContent": law.get("lawContent")
        })

    # -------------------------------
    # 4.获取申报材料
    # -------------------------------
    res_materials = requests.get(
        url=urlConfig.get("applicationMaterialsUrl"),
        params=params,
        headers=headers,
        timeout=30
    )
    data_materials = res_materials.json().get("data", {})

    application_materials = []

    directoryList = data_materials.get("directoryList") or []

    # 这种情况是既没有变更也没有其他的查询条件就需要获取noDirectoryList中的数据进行填充 命名为情况2
    if not directoryList:
        directoryList = data_materials.get("noDirectoryList") or []

    for directory in directoryList:
        # 判断是否为首次申请
        materialClass = directory.get("materialClass", {})
        situationTitle = 0 if materialClass.get("situationTitle") == "首次申请" else 1
        # 抽取申报材料信息(返回结果为列表形式)
        materialList = directory.get("material") or []

        # 下面这种是判断是否为情况2
        if not materialList and directory.get("materialName"):
            materialList = [directory]

        for material in materialList:
            application_materials.append({
                "unid": material.get("unid"),
                "situationTitle": situationTitle,
                # 文件类型
                "materialName": material.get("materialName"),
                # 材料形式(1-纸质，电子材料 2-电子材料 3-纸质 7-电子材料)
                "materialOrdernum": material.get("materialOrdernum"),
                # 材料要求(材料类型 份数)
                # 类型
                "materialMedium": material.get("materialMedium"),
                # 份数
                "materialPagenum": material.get("materialPagenum"),
                # 材料必要性(1-必要)
                "materialIsneed": material.get("materialIsneed"),
                # 来源渠道
                "materialSourcechannelName": material.get("materialSourcechannelName"),
                # 具体要求
                "materialPageformat": material.get("materialPageformat"),
                # 设立依据
                "materialLaw": material.get("materialLaw"),
                # 材料核查标准
                "material_check_standard": deal_material_check_standard(material.get("unid")),
                # 附件下载
                # 格式文本
                "materialFormguid": download_file(material.get("materialFormguid")) if material.get("materialFormguid") else None,
                # 示范文本
                "materialExampleguid": download_file(material.get("materialExampleguid")) if material.get("materialExampleguid") else None
            })

    # -------------------------------
    # 返回统一结构
    # -------------------------------
    return {
        "basic": basic,
        "basic_picture": basic_picture,
        "special": special,
        "laws": laws,
        "application_materials": application_materials
    }


def deal_material_check_standard(id):
    rpName = ""
    params = parameter["materialCheckStandard"].copy()
    params["materialUnid"] = id
    time.sleep(random.randint(4, 8))
    res = requests.get(
        url=urlConfig.get("materialCheckStandardUrl"),
        params=params,
        headers=headers,
        timeout=30
    )
    resJson = res.json()
    datas = resJson.get("data", {})
    if datas:
        for data in datas:
            rpName += data.get("rpName") if data.get("rpName") else ""

    return rpName

# 下载附件
def download_file(id):
    params = parameter["downloadAttachment"].copy()
    params["unid"] = id
    time.sleep(random.randint(4, 8))
    res = requests.get(
        url=urlConfig.get("downloadAttachmentUrl"),
        params=params,
        headers=headers,
        timeout=30
    )
    resJson = res.json()
    file_url = resJson.get("data")
    #下载文件内容（以二进制形式）
    file_response = requests.get(file_url, headers=headers, timeout=30)
    # 获取二进制内容
    binary_content = file_response.content

    return binary_content

def deal_basic_picture(imgfile, wordfile):
    # 只保留是字典类型，并且包含必要字段的项
    imgFile = cleaned_imgfile(imgfile)
    iwordfile = cleaned_imgfile(wordfile)
    imgFile.extend(iwordfile)

    result = {}
    for imgWordFile in imgFile:
        if imgWordFile:
            fileName = imgWordFile.get("fileName")
            fileUnid = imgWordFile.get("fileUnid")
            binary_content = download_file(fileUnid)
            result[fileName] = binary_content

    return result

# 只保留字典类型的数据
def cleaned_imgfile(imgfile):
    # 判断一下这个东西是不是只有元组，如果是元组，取第0个
    if isinstance(imgfile, tuple):
        imgfile = imgfile[0] if len(imgfile) > 0 else {}

    cleaned_imgfile = [item for item in imgfile if isinstance(item, dict) and item.get("fileName") and item.get("fileUnid")]
    return cleaned_imgfile