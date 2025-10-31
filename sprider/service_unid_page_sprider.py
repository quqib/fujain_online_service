"""
业务办理页面爬虫程序
"""
"""
获取三级页面的页面信息 按照要求不包括页脚的跳转链接内的信息
"""
import random
import time

import requests
from config.seetings import headers, urlConfig, parameter


def service_get_message(unid):
    # -------------------------------
    # 1️.业务办理-获取基础信息
    # -------------------------------
    params_basic = parameter["serviceUnidPage"].copy()
    params_basic["unid"] = unid

    res_basic = requests.get(
        url=urlConfig.get("serviceUnidPageUrl"),
        params=params_basic,
        headers=headers,
        timeout=30
    )
    data_basic = res_basic.json().get("data", {})
    apasDirectory = data_basic.get("apasDirectory", {})
    rspApasServiceExtend = data_basic.get("rspApasServiceExtend", {})
    service_basic = {
        "unid": apasDirectory.get("unid"),
        # 用于外键
        "basic_info_rowguid": unid,
        # 事项编码
        "infoprojid": apasDirectory.get("infoprojid"),
        # 基本编码
        "baseCode": apasDirectory.get("baseCode"),
        # 实施编码
        "implCode": apasDirectory.get("implCode"),
        # 业务办理项编码
        "taskHandleItem": apasDirectory.get("taskHandleItem"),

        # 办件类型
        "servicetype": apasDirectory.get("servicetype"),
        # 事项类型
        "addTypeName": apasDirectory.get("addTypeName"),
        # 行使层级
        "performLevelName": apasDirectory.get("performLevelName"),
        # 法定时限
        "lawlimit": apasDirectory.get("lawlimit"),
        # 承诺时限
        "promiseday": apasDirectory.get("promiseday"),
        # 实施主体
        "deptname": apasDirectory.get("deptname"),
        # 承诺时限说明
        "promisdayinfo": apasDirectory.get("promisdayinfo"),


        # 实施主体性质
        "deptPropertyName": apasDirectory.get("deptPropertyName"),
        # 委托部门
        "deptEntrust": apasDirectory.get("deptEntrust"),
        # 联办机构
        "dirName": apasDirectory.get("dirName"),
        # 主办处室
        "leadDept": apasDirectory.get("leadDept"),

        # 权力来源
        "rightSourceName": apasDirectory.get("rightSourceName"),
        # 联系电话
        "contactphone": apasDirectory.get("contactphone"),
        # 监督投诉电话
        "monitorcomplain": apasDirectory.get("monitorcomplain"),

        # 特殊环节
        "specialMode": apasDirectory.get("specialMode"),
        # 特殊环节-环节名称

        # 特殊环节-环节时限

        # 特殊环节-设定依据

        # 特殊环节-备注


        # 一件事集成套餐
        "dirName": apasDirectory.get("dirName"),

        # 市场准入负面清单许可准入措施(这里返回的也是一个列表，需要处理unid name表数据写入)
        "marketAccessList": apasDirectory.get("marketAccessList"),

        # 中介服务
        "dirName": apasDirectory.get("dirName"),
        # 权责清单
        "liabilityName": apasDirectory.get("liabilityName"), # 权责清单名称

        # 审批结果名称
        "resultName": apasDirectory.get("resultName"),
        # 审批结果类型
        "finishTypeName": apasDirectory.get("finishTypeName"),
        # 审批结果样本 (一个用于下载的字典)
        "resultFile": apasDirectory.get("resultFile"),
        # 审批结果共享
        "dirName": apasDirectory.get("dirName"),
        # 结果领取方式
        "finishGetTypeName": apasDirectory.get("finishGetTypeName"),
        # 结果领取说明
        "finishInfo": apasDirectory.get("finishInfo"),

        # 申报对象
        "userType": apasDirectory.get("userType"),

        # 是否进驻政务大厅
        "dirName": apasDirectory.get("dirName"),
        # 办理形式
        "handleForm": apasDirectory.get("handleForm"),
        # 必须现场办理原因
        "sceneReason": apasDirectory.get("sceneReason"),

        # 个人办事主题
        "gerenTheme": apasDirectory.get("gerenTheme"),
        # 企业办事主题
        "qiyeTheme": apasDirectory.get("qiyeTheme"),
        # 网上办理深度
        "webApplyDegreeName": apasDirectory.get("webApplyDegreeName"),

        # 通办范围
        "nearbyAreaName": apasDirectory.get("nearbyAreaName"),
        # 数量限制
        "countLimit": apasDirectory.get("countLimit"),
        # 通办范围说明
        "nearbyInstruction": apasDirectory.get("nearbyInstruction"),

        # 是否全国高频“跨省通办”事项
        "dirName": apasDirectory.get("dirName"),
        # 跨省通办模式
        "dirName": apasDirectory.get("webApplyDegreeName"),
        # 跨省代收代办区域
        "dirName": apasDirectory.get("dirName"),

        # 计划生效日期
        "planEnableDate": apasDirectory.get("planEnableDate"),
        # 计划取消日期
        "planCancelDate": apasDirectory.get("planCancelDate"),

        # 是否开通预约服务
        "dirName": apasDirectory.get("dirName"),
        # 是否支持自助终端办理
        "dirName": apasDirectory.get("dirName"),
        # 面向自然人地方特色主题分类
        "personalThemeCategory": apasDirectory.get("personalThemeCategory"),
        # 面向法人地方特色主题分类
        "companyThemeCategory": apasDirectory.get("companyThemeCategory"),

        # 移动端是否对接单点登录
        "mobileSingleLogin": apasDirectory.get("mobileSingleLogin"),
        # 计算机端是否对接单点登录
        "pcSingleLogin": apasDirectory.get("pcSingleLogin"),

        # 乡镇街道名称
        "smallTownsName": apasDirectory.get("smallTownsName"),
        # 乡镇街道代码
        "smallTownsCode": apasDirectory.get("smallTownsCode"),
        # 村镇社区名称
        "communityName": apasDirectory.get("communityName"),
        # 村镇社区代码
        "communityCode": apasDirectory.get("communityCode"),

        # 是否支持物流快递
        "logisticsExpress": apasDirectory.get("logisticsExpress"),
        # 是否支持网上支付
        "onlinePay": apasDirectory.get("onlinePay"),

        # 事项状态
        "state": apasDirectory.get("state"),
        # 是否全程代办
        "dirName": apasDirectory.get("dirName"),

        # 备注
        "iremark": apasDirectory.get("iremark"),
        # 是否收费
        "chargeLimit": apasDirectory.get("chargeLimit"),

        # 链接
        "dirLink": f"https://zwfw.fujian.gov.cn/standartCatalogGuide?unid={apasDirectory.get('unid')}"
    }


    # -------------------------------
    # 2.业务办理-市场准入负面清单许可准入措施
    # -------------------------------
    service_market_access = []

    marketAccessList = apasDirectory.get("marketAccessList")
    for marketAccess in marketAccessList:
        params_market_access = parameter["marketAccess"].copy()
        params_market_access["id"] = marketAccess.get("unid")

        res_market_access = requests.get(
            url=urlConfig.get("marketAccessUrl"),
            params=params_market_access,
            headers=headers,
            timeout=30
        )
        data_market_access = res_market_access.json().get("data", {})
        # 基础信息
        negativeList = data_market_access.get("negativeList", {})
        # 措施信息
        measures = data_market_access.get("measures", {})
        # 措施匹配
        catalogVos = data_market_access.get("catalogVos", [])
        measureMatching = "!@#".join([catalogVo.get("dirName") for catalogVo in catalogVos])
        service_market_access.append({
            # 名称
            "name": marketAccess.get("unid"),
            # 基础信息
            # 负面清单事项版本
            "negativeList_status": negativeList.get("status"),
            # 负面清单类别
            "negativeList_itemType": negativeList.get("itemType"),
            # 行业（领域、来源）类别
            "negativeList_industryType": negativeList.get("industryType"),
            # 负面清单事项名称
            "negativeList_name": negativeList.get("name"),
            # 负面清单事项编码
            "negativeList_code": negativeList.get("code"),

            # 措施信息
            # 负面清单事项措施名称
            "measures_name": measures.get("name"),
            # 负面清单事项措施编码
            "measures_code": measures.get("code"),
            # 地方性许可措施
            "localLicensingMeasures": measures.get("localLicensingMeasures"),
            # 适用范围
            "": measures.get(""),
            # 事项措施状态
            "": measures.get("status"),
            # 负面清单事项措施版本
            "": measures.get("version"),
            # 是否暂时列入清单
            "": measures.get(""),
            # 计划生效日期
            "takeEffectDate": measures.get("takeEffectDate"),
            # 计划取消日期
            "cancelDate": measures.get("cancelDate"),

            # 措施匹配
            "measureMatching": measureMatching,
        })


    # -------------------------------
    # 3.业务办理-权责清单
    # -------------------------------
    params_responsibity_author = parameter["responsibilityAuthorities"].copy()
    params_responsibity_author["powerunid"] = unid

    res_responsibity_author= requests.get(
        url=urlConfig.get("responsibilityAuthoritiesUrl"),
        params=params_responsibity_author,
        headers=headers,
        timeout=30
    )
    data_responsibity_author = res_responsibity_author.json().get("data", {})
    # 关联服务事项名称列表集合
    apaserviceList = data_responsibity_author.get("apaserviceList")
    # 权责清单
    service_responsibity_author = {
        # 类别
        "stype": data_responsibity_author.get("stype"),
        # 权责编码
        "mattercode": data_responsibity_author.get("mattercode"),
        # 关联服务事项名称
        "apaservice_name": "!@#".join([apaservice.get("name") for apaservice in apaserviceList]),
        # 行使主体
        "deptname": data_responsibity_author.get("deptname"),
        # 行使层级
        "xslevel": data_responsibity_author.get("xslevel"),
        # 实施依据
        "according": data_responsibity_author.get("according"),
        # 备注
        "remark": data_responsibity_author.get("remark"),
    }


    # -------------------------------
    # 4.业务办理-受理条件 窗口办理
    # -------------------------------
    applyMethod = data_basic.get("applyMethod", {})
    service_apply = {
        # 办理时间
        "officeTime": applyMethod.get("officeTime"),
        # 办理地点
        "acceptAddress": applyMethod.get("acceptAddress"),
        # 交通指引
        "trafficGuide": applyMethod.get("trafficGuide"),
        # 受理条件
        "applyTerm": applyMethod.get("applyMethod"),
    }



    # -------------------------------
    # 5.业务办理-办理流程
    # -------------------------------
    params_processing_procedure = parameter["processingProcedure"].copy()
    params_processing_procedure["serviceId"] = unid

    res_processing_procedure = requests.get(
        url=urlConfig.get("processingProcedureUrl"),
        params=params_processing_procedure,
        headers=headers,
        timeout=30
    )
    processing_procedures = res_processing_procedure.json().get("data", {}).get("flowNodeList", [])
    service_processing_procedure = []
    for processing_procedure in processing_procedures:
        service_processing_procedure.append({
            # 办理流程(申请与受理|审查|决定)
            "name": processing_procedure.get("name"),
            # 步骤类型
            "step": processing_procedure.get("step"),
            # 办理人
            "nodeoperator": processing_procedure.get("nodeoperator"),
            # 办理时限(当场 如果是工作日需要进行拼接 limitcount)
            "limittype": str(processing_procedure.get("limitcount"))+processing_procedure.get("limittype")
            if processing_procedure.get("limitcount") else processing_procedure.get("limittype"),
            # 审查标准
            "csstandard": processing_procedure.get("csstandard"),
            # 办理结果
            "transactresult": processing_procedure.get("transactresult"),
        })


    # -------------------------------
    # 6.业务办理-网上办理
    # -------------------------------
    params_online = parameter["onlineUnidPage"].copy()
    params_online["unid"] = unid

    res_online = requests.get(
        url=urlConfig.get("onlineUnidPageUrl"),
        params=params_online,
        headers=headers,
        timeout=30
    )
    data_online = res_online.json().get("data", {})

    service_onlines = []
    for online in data_online:
        online_dict = online.get("dict")
        accept = 1 if online.get("accept") else 0
        service_onlines.append({
            # 是否涉及 0 否， 1 是
            "accept": accept,
            # 网上申请方式
            "dictname": online_dict.get("dictname"),
            # 账户要求
            "accountTypeName": online.get("accept").get("accountTypeName")if accept else "无",
            # 承诺到窗口最多次说明
            "towininfo": online.get("accept").get("towininfo")if accept else None,
        })


    # -------------------------------
    # 7.业务办理-办理依据
    # -------------------------------
    service_handling = {
        "according": data_basic.get("data_basic")
    }


    # -------------------------------
    # 8.业务办理-常见问题
    # -------------------------------
    params_asked_questions = parameter["frequentlyAskedQuestions"].copy()
    params_asked_questions["unid"] = unid

    res_asked_questions = requests.get(
        url=urlConfig.get("frequentlyAskedQuestionsUrl"),
        params=params_asked_questions,
        headers=headers,
        timeout=30
    )
    data_asked_questions = res_asked_questions.json().get("data", {})
    service_asked_question = []
    for data_asked_question in data_asked_questions:
        service_asked_question.append({
            # 问题标题
            "title": data_asked_question.get("title"),
            # 问题内容
            "content": data_asked_question.get("content")
        })


    # -------------------------------
    # 返回统一结构
    # -------------------------------
    return {
        # 基本信息
        "service_basic": service_basic,
        # 市场准入负面清单许可准入措施
        "service_market_access": service_market_access,
        # 权责清单
        "service_responsibity_author": service_responsibity_author,
        # 窗口办理+受理条件
        "service_apply": service_apply,
        # 网上办理
        "service_onlines": service_onlines,
        # 办理流程
        "service_processing_procedure": service_processing_procedure,
        # 常见问题
        "service_asked_question": service_asked_question,
        # 办理依据
        "service_handling": service_handling,
    }



service_get_message(unid="F8B0582A365552FB9247B678A952D7AF")



def deal_material_check_standard(id):
    rpName = ""
    params = parameter["materialCheckStandard"].copy()
    params["materialUnid"] = id
    # time.sleep(random.randint(2, 3))
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
    time.sleep(random.randint(1, 3))
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

# 处理图片信息
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


# 处理业务办理-基本信息-特殊环节
def get_special_list(specialList):

    for i, value in enumerate(specialList):

        pass


# 获取网上办理信息
def get_onlion_message(data_online):

    pass
