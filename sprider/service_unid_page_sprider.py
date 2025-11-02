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

    # 获取页面相关的附件用于后续附件的检索
    data_attachment_information = get_attachment_information(unid)

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

        # 办件类型()
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
        # 联办机构 当servicetype为联办件的时候才会显示
        "coopOrg": apasDirectory.get("coopOrg"),
        # 主办处室
        "leadDept": apasDirectory.get("leadDept"),

        # 权力来源
        "rightSourceName": apasDirectory.get("rightSourceName"),
        # 联系电话
        "contactphone": apasDirectory.get("contactphone"),
        # 监督投诉电话
        "monitorcomplain": apasDirectory.get("monitorcomplain"),


        # 一件事集成套餐
        # "dirName": apasDirectory.get("dirName"),

        # 市场准入负面清单许可准入措施(这里返回的也是一个列表，需要处理unid name表数据写入)
        "marketAccessList": apasDirectory.get("marketAccessList"),

        # 中介服务 注意这个是个列表
        "intermediaryServicesList": apasDirectory.get("intermediaryServicesList"),
        # 权责清单
        "liabilityName": apasDirectory.get("liabilityName"), # 权责清单名称

        # 审批结果名称
        "resultName": apasDirectory.get("resultName"),
        # 审批结果类型
        "finishTypeName": apasDirectory.get("finishTypeName"),
        # 审批结果样本 (一个用于下载的字典)
        "resultFile": apasDirectory.get("resultFile"),
        # 审批结果共享(有值是 无值否)
        "finishType": apasDirectory.get("finishType"),
        # 结果领取方式
        "finishGetTypeName": apasDirectory.get("finishGetTypeName"),
        # 结果领取说明
        "finishInfo": apasDirectory.get("finishInfo"),

        # 申报对象
        "userType": apasDirectory.get("userType"),

        # 是否进驻政务大厅 0否 1是
        "enterif": apasDirectory.get("enterif"),
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
        "highFrequencyKstb": apasDirectory.get("highFrequencyKstb"),
        # 跨省通办模式说明
        "kstbModel": rspApasServiceExtend.get("kstbModel"),
        # 跨省代收代办区域
        "kstbOutAreaname": apasDirectory.get("kstbOutAreaname"),

        # 计划生效日期
        "planEnableDate": apasDirectory.get("planEnableDate"),
        # 计划取消日期
        "planCancelDate": apasDirectory.get("planCancelDate"),

        # 是否开通预约服务
        "isSubscribeService": apasDirectory.get("isSubscribeService"),
        # 是否支持自助终端办理
        "terminalSupport": apasDirectory.get("terminalSupport"),
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
        # 是否全程代办 N代表否 Y代表是
        "agentFlag": apasDirectory.get("agentFlag"),

        # 备注
        "iremark": apasDirectory.get("iremark"),
        # 是否收费
        "chargeLimit": apasDirectory.get("chargeLimit"),

        # 链接
        "dirLink": f"https://zwfw.fujian.gov.cn/standartCatalogGuide?unid={apasDirectory.get('unid')}"
    }

    # -------------------------------
    # 2.业务办理-特殊环节
    # -------------------------------
    specialList = apasDirectory.get("specialList")
    service_section_list = []

    for special in specialList:
        service_section_list.append({
            # 环节名称
            "sname": special.get("sname"),
            # 环节时限
            "sday": special.get("sday"),
            # 环节依据
            "sconent": special.get("sconent"),
            # 备注
            "sremark": special.get("sremark"),
        })

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
            "localLicensing": measures.get("localLicensing"),
            # 适用范围
            "scope": measures.get("scope"),
            # 事项措施状态
            "status": measures.get("status"),
            # 负面清单事项措施版本
            "version": measures.get("version"),
            # 是否暂时列入清单
            "included": measures.get("included"),
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
    # 3.业务办理-申请材料
    # -------------------------------
    params_materials = parameter["sriviceApplicationMaterials"].copy()
    params_materials["unid"] = unid
    res_materials = requests.get(
        url=urlConfig.get("sriviceApplicationMaterialsUrl"),
        params=params_materials,
        headers=headers,
        timeout=30
    )
    data_materials = res_materials.json().get("data", {})

    # 用来存储申报材料信息
    service_application_materials = []
    # 用来存储核查信息
    service_material_verifications = []

    directoryList = data_materials.get("directoryList") or []

    # 这种情况是既没有变更也没有其他的查询条件就需要获取noDirectoryList中的数据进行填充 命名为情况2
    if not directoryList:
        directoryList = data_materials.get("noDirectoryList") or []

    # 对directoryList进行去重处理
    materialCheckList = material_check_list(directoryList)

    # 递归处理children 获取application_materials
    get_application_materials(materialCheckList,
                              service_application_materials,
                              service_material_verifications,
                              data_attachment_information)


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
        # 特殊环节
        "service_section_list": service_section_list,
        # 市场准入负面清单许可准入措施
        "service_market_access": service_market_access,
        # 权责清单
        "service_responsibity_author": service_responsibity_author,
        # 申报材料
        "service_application_materials": service_application_materials,
        # 申报材料——核查数据
        "service_material_verifications": service_material_verifications,
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



# service_get_message(unid="F8B0582A365552FB9247B678A952D7AF")



def deal_material_check_standard(id):
    rpName = ""
    params = parameter["materialCheckStandard"].copy()
    params["materialUnid"] = id
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

# 获取所有的附件信息
def get_attachment_information(id):
    params_attachment_information = parameter["getAttachmentInformation"].copy()
    params_attachment_information["serviceId"] = "F8B0582A365552FB9247B678A952D7AF"
    res_attachment_information = requests.get(
        url=urlConfig.get("getAttachmentInformationUrl"),
        params=params_attachment_information,
        headers=headers,
        timeout=30
    )
    data_attachment_information = res_attachment_information.json().get("data").get("tableList")

    return data_attachment_information

# 检索出相关的附件
def get_check_attachment(data_list, target_punid, type):
    # type 1样表 2空表
    return [
            item.get("fileunid")
        for item in data_list
        if item.get("punid") == target_punid and int(item.get("type")) == type
    ]


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

# 请求——材料核查标准
def res_message_children(itemUnid, materialName, materialUnid):
    params_material_erification = parameter["materialVerificationInformation"].copy()
    params_material_erification["itemUnid"] = itemUnid
    params_material_erification["materialName"] = materialName
    params_material_erification["materialUnid"] = materialUnid

    res_material_erification = requests.post(
        url=urlConfig.get("materialVerificationInformationUrl"),
        json=params_material_erification,
        headers=headers,
        timeout=30
    )

    return res_material_erification.json().get("data")

# 抽取申报材料——材料核查标准
def get_message_children(data, all_node):
    childProblems = data.get("childProblems") if data.get("childProblems") else []
    # 获取本身节点id
    problemUnid = data.get("problemUnid")
    # 获取父节点
    parentProblemUnid = data.get("parentProblemUnid")
    # 获取段落文本
    problemName = data.get("problemName")

    # 材料标识
    materialUnid = data.get("materialUnid")

    for childProblem in childProblems:
        get_message_children(childProblem, all_node=all_node)

    all_node.append({
        # 材料标识
        "materialUnid": materialUnid,
        # 本身节点
        "problemUnid": problemUnid,
        # 父级节点
        "parentProblemUnid": parentProblemUnid,
        # 本身字段
        "problemName": problemName,
    })

# 申报材料——中发现重复，进行去重处理
def material_check_list(directoryList):
    materialCheckList = []
    seen_unids = set()  # 用于记录已添加的 material unid

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
            unid = material.get("unid")
            material['situationTitle'] = situationTitle

            # 如果 unid 已存在，则跳过
            if unid in seen_unids:
                continue

            # 否则，标记为已见过，并添加到结果列表
            seen_unids.add(unid)
            materialCheckList.append(material)

    return materialCheckList


# 申报材料——递归处理children
def get_application_materials(materialList,
                              application_materials,
                              all_data,
                              data_attachment_information,
                              parent_unid=None):

    for material in materialList:
        children = material.get("children")
        if children:
            # 添加父节点
            application_materials.append({
                "unid": material.get("unid"),
                "name": material.get("name"),
            })

            # 递归处理子节点，将当前节点的unid作为父unid传递
            get_application_materials(children,
                                      application_materials=application_materials,
                                      all_data=all_data,
                                      data_attachment_information=data_attachment_information,
                                      parent_unid=material.get("unid")
                                      )

        else:
            # 请求链接获取材料核查标准信息
            data_material_erification = res_message_children("F8B0582A365552FB9247B678A952D7AF",
                                                             material.get("name"),
                                                             material.get("unid"))
            # 解析核查标准信息
            get_message_children(data_material_erification, all_data)

            application_materials.append({
                "unid": material.get("unid"),
                # 增加一个父节点
                "parentUnid": parent_unid,
                # 是否为首次申请
                "situationTitle": material.get("situationTitle"),
                # 文件类型
                "materialName": material.get("name"),
                # 材料形式(电子上传-upload,电子共享材料-license,paper-纸质")
                "gettypeunids": material.get("gettypeunids"),
                # 材料要求(材料类型 份数)
                # 类型
                "medium": material.get("medium"),
                # 份数(如果类型是复印件使用参数pagecopynum)
                "pagenum": material.get("pagecopynum") if material.get("medium")=="复印件" else material.get("pagenum"),
                # 材料必要性(1-必要 2-非必要)
                "necessityIf": material.get("necessityIf"),
                # 来源渠道
                "materialsrc": material.get("materialsrc"),
                # 设立依据
                "applyAccord": material.get("applyAccord"),
                # 填报须知
                "reportNotice": material.get("reportNotice"),
                # 材料核查单独存表
                # 附件下载
                # 格式文本
                "materialFormguid": download_file(
                    get_check_attachment(data_attachment_information, material.get("unid"), type=2
                                         )[0]),
                # 示范文本
                "materialExampleguid": download_file(
                    get_check_attachment(data_attachment_information, material.get("unid"), type=1
                                         )[0])
            })


