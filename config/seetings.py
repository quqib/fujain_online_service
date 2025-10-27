# 数据库连接配置
# DB_CONFIG = {
#     'host': '172.16.30.106',
#     'port': 3306,
#     'user': 'root',
#     'password': 'root123',
#     'database': 'online_service',
#     'charset': 'utf8mb4'
# }

DB_CONFIG = {
    'host': '192.168.10.110',
    'port': 3306,
    'user': 'root',
    'password': 'root123',
    'database': 'online_service',
    'charset': 'utf8mb4'
}


# 构建数据库 URL
DATABASE_URL = f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@" \
               f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}?" \
               f"charset={DB_CONFIG['charset']}"


headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Origin': 'https://zwfw.fujian.gov.cn',
    'Referer': 'https://zwfw.fujian.gov.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}

# 用于请求获取页面上的基本信息链接
urlConfig = {
    # 二级页面链接
    "secondaryPageUrl": "https://zwfw.fujian.gov.cn:732/cms-business/listingService/getBzhSxInfoList",
    # 链接获取信息(基本信息 特殊环节 设立依据) GET
    "basicInformationUrl": "https://zwfw.fujian.gov.cn:732/cms-business/apasDirectory/getDireBasicInfo",
    # 链接获取信息(申报材料) GET
    "applicationMaterialsUrl": "https://zwfw.fujian.gov.cn:732/cms-business/apasDirectory/getDirMaterialList",
    # 下载附件链接 GET
    "downloadAttachmentUrl": "https://zwfw.fujian.gov.cn:732/cms-business/apasService/file/downloadFile"
}

# 请求过程中的参数
parameter = {
    # 二级页面请求参数信息
    "secondaryPage": {
        "stype": "01",
        "deptUnid": "",
        "subname": "",
        "pageSize": "10",
        "pageNum": "1",
        "performLevel": ""
    },

    # 基本信息 特殊环节信息 具体页面
    "basicInformation": {
        "unid": "",
    },

    # 申报材料参数信息
    "applicationMaterials": {
        "unid": "",
        "situationUnid": "",
        "isMatmultiple": "Y"
    },

    # 下载附件参数信息
    "downloadAttachment": {
        "unid":""
    },
}


# 用于测试的参数数据
params = {
    'unid': '5EA0B30916E33C9D326AAE92D6AF3D96',
}

