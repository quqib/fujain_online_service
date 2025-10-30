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
    params = parameter["serviceUnidPage"].copy()
    params["unid"] = unid

    res_basic = requests.get(
        url=urlConfig.get("serviceUnidPageUrl"),
        params=params,
        headers=headers,
        timeout=30
    )
    data_basic = res_basic.json().get("data", {})
    apasDirectory = data_basic.get("apasDirectory", {})
    service_basic = {
        "unid": apasDirectory.get("unid"),

        # 事项编码
        "item_code": apasDirectory.get("infoprojid"),
        # 基本编码
        "basic_code": apasDirectory.get("baseCode"),
        # 实施编码
        "implement_code": apasDirectory.get("implCode"),
        # 业务办理项编码
        "dirPromiseday": apasDirectory.get("taskHandleItem"),

        # 办件类型
        "handling_type": apasDirectory.get("servicetype"),
        # 事项类型
        "dirCode": apasDirectory.get("addTypeName"),
        # 行使层级
        "handleContent": apasDirectory.get("performLevelName"),
        # 法定时限
        "handleLaw": apasDirectory.get("lawlimit"),
        # 承诺时限
        "chargeFlag": apasDirectory.get("promiseday"),
        # 实施主体
        "chargeItems": apasDirectory.get("deptname"),
        # 承诺时限说明
        "chargeFlag": apasDirectory.get("promisdayinfo"),


        # 实施主体性质
        "dirName": apasDirectory.get("deptPropertyName"),
        # 委托部门
        "dirName": apasDirectory.get("dirName"),
        # 联办机构
        "dirName": apasDirectory.get("dirName"),
        # 主办处室
        "dirName": apasDirectory.get("leadDept"),

        # 权力来源
        "dirName": apasDirectory.get("rightSourceName"),
        # 联系电话
        "dirName": apasDirectory.get("contactphone"),
        # 监督投诉电话
        "dirName": apasDirectory.get("monitorcomplain"),

        # 特殊环节
        "dirName": apasDirectory.get("dirName"),
        # 特殊环节-环节名称

        # 特殊环节-环节时限

        # 特殊环节-设定依据

        # 特殊环节-备注


        # 一件事集成套餐
        "dirName": apasDirectory.get("dirName"),

        # 市场准入负面清单许可准入措施(这里返回的也是一个列表，需要处理unid name进行如表)
        "dirName": apasDirectory.get("marketAccessList"),

        # 中介服务
        "dirName": apasDirectory.get("dirName"),
        # 权责清单
        "dirName": apasDirectory.get("liabilityName"), # 权责清单名称

        # 审批结果名称
        "dirName": apasDirectory.get("resultName"),
        # 审批结果类型
        "dirName": apasDirectory.get("finishTypeName"),
        # 审批结果样本 (一个用于下载的字典)
        "dirName": apasDirectory.get("resultFile"),
        # 审批结果共享
        "dirName": apasDirectory.get("dirName"),
        # 结果领取方式
        "dirName": apasDirectory.get("finishGetTypeName"),
        # 结果领取说明
        "dirName": apasDirectory.get("finishInfo"),

        # 申报对象
        "dirName": apasDirectory.get("userType"),

        # 是否进驻政务大厅
        "dirName": apasDirectory.get("dirName"),
        # 办理形式
        "dirName": apasDirectory.get("handleForm"),
        # 必须现场办理原因
        "dirName": apasDirectory.get("dirName"),

        # 企业办事主题
        "dirName": apasDirectory.get("qiyeTheme"),
        # 网上办理深度
        "dirName": apasDirectory.get("webApplyDegreeName"),

        # 通办范围
        "dirName": apasDirectory.get("nearbyAreaName"),
        # 数量限制
        "dirName": apasDirectory.get("countLimit"),
        # 通办范围说明
        "dirName": apasDirectory.get("nearbyInstruction"),

        # 是否全国高频“跨省通办”事项
        "dirName": apasDirectory.get("dirName"),
        # 跨省通办模式
        "dirName": apasDirectory.get("dirName"),
        # 跨省代收代办区域
        "dirName": apasDirectory.get("dirName"),

        # 计划生效日期
        "dirName": apasDirectory.get("dirName"),
        # 计划取消日期
        "dirName": apasDirectory.get("dirName"),

        # 是否开通预约服务
        "dirName": apasDirectory.get("dirName"),
        # 是否支持自助终端办理
        "dirName": apasDirectory.get("dirName"),
        # 面向法人地方特色主题分类
        "dirName": apasDirectory.get("dirName"),

        # 移动端是否对接单点登录
        "dirName": apasDirectory.get("dirName"),
        # 计算机端是否对接单点登录
        "dirName": apasDirectory.get("dirName"),

        # 乡镇街道名称
        "dirName": apasDirectory.get("dirName"),
        # 乡镇街道代码
        "dirName": apasDirectory.get("dirName"),
        # 村镇社区名称
        "dirName": apasDirectory.get("dirName"),
        # 村镇社区代码
        "dirName": apasDirectory.get("dirName"),

        # 是否支持物流快递
        "dirName": apasDirectory.get("dirName"),
        # 是否支持网上支付
        "dirName": apasDirectory.get("dirName"),

        # 事项状态
        "dirName": apasDirectory.get("state"),
        # 是否全程代办
        "dirName": apasDirectory.get("dirName"),

        # 备注
        "dirName": apasDirectory.get("iremark"),
        # 是否收费
        "chargeLimit": apasDirectory.get("chargeLimit"),
        # 常见问题
        "dirName": apasDirectory.get("dirName"),
        # 链接
        "dirLink": f"https://zwfw.fujian.gov.cn/standartCatalogGuide?unid={apasDirectory.get('unid')}"
    }

    # -------------------------------
    # 2.业务办理-受理条件 窗口办理
    # -------------------------------
    applyMethod = data_basic.get("applyMethod", {})
    service_apply = {
        # 受理条件
        "applyTerm": applyMethod.get("applyMethod"),
        # 办理时间
        "officeTime": applyMethod.get("officeTime"),
        # 办理地点
        "acceptAddress": applyMethod.get("acceptAddress"),
        # 交通指引
        "trafficGuide": applyMethod.get("trafficGuide")
    }


    # -------------------------------
    # 3.业务办理-申报材料
    # -------------------------------


    # -------------------------------
    # 4.业务办理-办理流程
    # -------------------------------


    # -------------------------------
    # 5.业务办理-窗口办理
    # -------------------------------


    # -------------------------------
    # 6.业务办理-网上办理
    # -------------------------------
    params = parameter["onlineUnidPage"].copy()
    params["unid"] = unid

    res_online = requests.get(
        url=urlConfig.get("onlineUnidPageUrl"),
        params=params,
        headers=headers,
        timeout=30
    )
    data_online = res_online.json().get("data", {})



    # -------------------------------
    # 7.业务办理-办理依据
    # -------------------------------


    # -------------------------------
    # 8.业务办理-常见问题
    # -------------------------------



    # -------------------------------
    # 返回统一结构
    # -------------------------------

    return {
        "service_basic": service_basic,
        "service_apply": service_apply,
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
def get_onlion_message():

    pass
