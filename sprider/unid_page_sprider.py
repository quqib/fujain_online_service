"""
获取三级页面的页面信息 按照要求不包括页脚的跳转链接内的信息
"""
import requests
from config.seetings import headers, urlConfig, parameter


def get_messsage(unid):
    # 拷贝一份 basicInformation 参数模板
    params = parameter["basicInformation"].copy()

    # 动态注入 unid
    params["unid"] = unid

    res = requests.get(
        url=urlConfig.get("basicInformationUrl"),
        params=params,
        headers=headers,
    )
    resJson = res.json()

    """
    基本信息
    """
    apasDirectory = resJson.get("data").get("apasDirectory")
    # 事项类型
    dirType = apasDirectory.get("dirType")
    # 行使层级(3-市级, 4-县级)
    dirUseLevel = apasDirectory.get("dirUseLevel")
    # 法定时限(多少个工作日)
    dirAnticipateday = apasDirectory.get("dirAnticipateday")
    # 承诺时限(多少个工作日)
    dirPromiseday = apasDirectory.get("dirPromiseday")
    # 部门名称
    deptName = apasDirectory.get("deptName")
    # 事项编码
    dirCode = apasDirectory.get("dirCode")
    # 办理条件
    handleContent = apasDirectory.get("handleContent")
    # 办理条件设立依据
    handleLaw = apasDirectory.get("handleLaw")
    # 是否收费

    # 办理流程图(jpg, pdf文件)
    imgfile = apasDirectory.get("imgfile")
    # 审批结果材料(word文件附件)
    wordfile = apasDirectory.get("wordfile")
    # 名称
    dirName = apasDirectory.get("dirName")
    # 链接
    dirLink = "https://zwfw.fujian.gov.cn/standartCatalogGuide?unid=" + apasDirectory.get("unid")


    """
    特殊环节
    """
    # 目前看到的都是单个数据,取第一个 可能为空
    specialList = resJson.get("data").get("specialList")[0]

    # 特殊环节名称
    specialName = specialList.get("specialName")
    # 承诺时限(多少个工作日)
    specialPromiseday = specialList.get("specialPromiseday")
    # 设立依据
    specialLaw = specialList.get("specialLaw")

    """
    设立依据
    """
    # 多个数据，需要循环进行存储
    lawList = resJson.get("data").get("lawList")
    law = lawList[0]
    # 依据文件名称
    lawName = law.get("lawName")
    # 依据文号
    lawSymbol = law.get("lawSymbol")
    # 颁布机关
    lawImplementdept = law.get("lawImplementdept")
    # 实施日期
    lawImplementdate = law.get("lawImplementdate")
    # 依据级别
    lawLevelName = law.get("lawLevelName")
    # 条款内容
    lawContent = law.get("lawContent")

def get_application_materials(unid):
    # 拷贝一份 basicInformation 参数模板
    params = parameter["basicInformation"].copy()

    # 动态注入 unid
    params["unid"] = unid

    res = requests.get(
        url=urlConfig.get("applicationMaterialsUrl"),
        params=params,
        headers=headers,
    )
    resJson = res.json()
    """
    申报材料(这部分需要另外一个链接)
    """
    # 分为两种首次申请和变更
    directoryList = resJson.get("data").get("directoryList")
    for i, directory in enumerate(directoryList):
        # 判断是否为首次申请
        materialClass = directory.get("materialClass")
        situationTitle = 0 if directory.get("situationTitle") == "首次申请" else 1
        # 抽取申报材料信息(返回结果为列表形式)
        materialList = directory.get("material")
        for material in materialList:
            # 文件类型
            materialName = material.get("materialName")
            # 材料形式(1-纸质，电子材料 3-纸质 7-电子材料)
            materialOrdernum = material.get("materialOrdernum")

            # 材料要求(材料类型 份数)
            # 类型
            materialMedium = material.get("materialMedium")
            # 份数
            materialPagenum = material.get("materialPagenum")

            # 材料必要性(1-必要)
            materialIsneed = material.get("materialIsneed")
            # 来源渠道
            materialSourcechannelName = material.get("materialSourcechannelName")
            # 具体要求
            materialPageformat = material.get("materialPageformat")
            # 设立依据
            materialLaw = material.get("materialLaw")
            # 材料核查标准  结果格式如下所示 GET (发送请求拼接链接https://zwfw.fujian.gov.cn:732/cms-business/apasDirectory/getReviewpoint?materialUnid=)
            """
            返回数据如下：
                {
                  "code": 200,
                  "msg": null,
                  "data": [
                    {
                      "unid": "104CCB75335D86040D50D749B019BE2C",
                      "parentName": null,
                      "parentUnid": null,
                      "rspReviewpoints": null,
                      "rpName": "是否项目单位申请。"
                    },
                    {
                      "unid": "18C7939DBCD969A994218467A1550790",
                      "parentName": null,
                      "parentUnid": null,
                      "rspReviewpoints": null,
                      "rpName": "是否简单介绍项目情况。"
                    },
                    {
                      "unid": "F4B2C714F26AEA5C819CA4056B01A10F",
                      "parentName": null,
                      "parentUnid": null,
                      "rspReviewpoints": null,
                      "rpName": "是否加盖企业公章。"
                    },
                    {
                      "unid": "6F2A2B2502AF7030F61E3D55C6E3894D",
                      "parentName": null,
                      "parentUnid": null,
                      "rspReviewpoints": null,
                      "rpName": "是否已取得工信系统的项目编码。"
                    }
                  ],
                  "total": null
                }
            """
            unid = material.get("unid")
            # 附件下载
            # 格式文本
            materialFormguid = material.get("materialFormguid")
            # 示范文本
            materialExampleguid = material.get("materialExampleguid")
            # 首次申请0 变更1






