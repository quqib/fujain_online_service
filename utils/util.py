import base64
import time
import urllib.parse


# 按照前段页面生成base64编码
def get_time_code():
    # Step 1: 获取当前时间戳（秒），转为字符串（10位）
    e = str(int(time.time()))  # 如: '1762060284'

    # Step 2: 取后3位（从第7位开始取3位，即倒数第3位开始）
    t = e[7:10]  # Python 字符串索引从0开始，[7:10] 取第8~10个字符（共3位）

    # Step 3: 重复3次并转为整数
    repeated_t = t + t + t  # 如 '123' → '123123123'
    num_repeated = int(repeated_t)

    # Step 4: 异或运算
    n = num_repeated ^ int(e)  # 异或：^

    # Step 5: 拼接字符串并进行 URI 编码（主要是处理可能的特殊字符）
    raw_string = f"{e}-{n}"
    uri_encoded = urllib.parse.quote(raw_string)  # 等价于 JS 的 encodeURI

    # Step 6: Base64 编码（btoa 是 base64 encode）
    b64_encoded = base64.b64encode(uri_encoded.encode('utf-8')).decode('utf-8')

    return b64_encoded



