"""
获取三级页面的页面信息 按照要求不包括页脚的跳转链接内的信息
"""
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
    )
    data_basic = res_basic.json().get("data", {})

    apasDirectory = data_basic.get("apasDirectory", {})
    basic = {
        "unid": apasDirectory.get("unid"),
        "dirType": apasDirectory.get("dirType"),
        "dirUseLevel": apasDirectory.get("dirUseLevel"),
        "dirAnticipateday": apasDirectory.get("dirAnticipateday"),
        "dirPromiseday": apasDirectory.get("dirPromiseday"),
        "deptName": apasDirectory.get("deptName"),
        "dirCode": apasDirectory.get("dirCode"),
        "handleContent": apasDirectory.get("handleContent"),
        "handleLaw": apasDirectory.get("handleLaw"),
        "imgfile": apasDirectory.get("imgfile"),
        "wordfile": apasDirectory.get("wordfile"),
        "dirName": apasDirectory.get("dirName"),
        "dirLink": f"https://zwfw.fujian.gov.cn/standartCatalogGuide?unid={apasDirectory.get('unid')}"
    }

    # -------------------------------
    # 2️.特殊环节
    # -------------------------------
    specialList = data_basic.get("specialList") or []
    special = {}
    if specialList:
        specialItem = specialList[0]
        special = {
            "specialName": specialItem.get("specialName"),
            "specialPromiseday": specialItem.get("specialPromiseday"),
            "specialLaw": specialItem.get("specialLaw")
        }

    # -------------------------------
    # 2️.设立依据
    # -------------------------------
    lawList = data_basic.get("lawList") or []
    laws = []
    for law in lawList:
        laws.append({
            "lawName": law.get("lawName"),
            "lawSymbol": law.get("lawSymbol"),
            "lawImplementdept": law.get("lawImplementdept"),
            "lawImplementdate": law.get("lawImplementdate"),
            "lawLevelName": law.get("lawLevelName"),
            "lawContent": law.get("lawContent")
        })

    # -------------------------------
    # 4.获取申报材料
    # -------------------------------
    res_materials = requests.get(
        url=urlConfig.get("applicationMaterialsUrl"),
        params=params,
        headers=headers,
    )
    data_materials = res_materials.json().get("data", {})

    application_materials = []

    directoryList = data_materials.get("directoryList") or []
    for directory in directoryList:
        materialClass = directory.get("materialClass")
        situationTitle = 0 if directory.get("situationTitle") == "首次申请" else 1
        materialList = directory.get("material") or []

        for material in materialList:
            application_materials.append({
                "unid": material.get("unid"),
                "materialClass": materialClass,
                "situationTitle": situationTitle,
                "materialName": material.get("materialName"),
                "materialOrdernum": material.get("materialOrdernum"),
                "materialMedium": material.get("materialMedium"),
                "materialPagenum": material.get("materialPagenum"),
                "materialIsneed": material.get("materialIsneed"),
                "materialSourcechannelName": material.get("materialSourcechannelName"),
                "materialPageformat": material.get("materialPageformat"),
                "materialLaw": material.get("materialLaw"),
                "materialFormguid": material.get("materialFormguid"),
                "materialExampleguid": material.get("materialExampleguid")
            })

    # -------------------------------
    # 返回统一结构
    # -------------------------------
    return {
        "basic": basic,
        "special": special,
        "laws": laws,
        "application_materials": application_materials
    }






