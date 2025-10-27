import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    # 'Cookie': 'JSESSIONID=C73BDA6745C582CA6DD1794A8AAB01F3; __51cke__=; suwellCookie=483e46d3-0e51-4957-995a-522275b2aba1; __tins__21889365=%7B%22sid%22%3A%201761548058002%2C%20%22vd%22%3A%2011%2C%20%22expires%22%3A%201761551340830%7D; __51laig__=31',
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

params = {
    'unid': '5EA0B30916E33C9D326AAE92D6AF3D96',
    'situationUnid': '',
    'isMatmultiple': 'Y',
}

res = requests.get(
    'https://zwfw.fujian.gov.cn:732/cms-business/apasDirectory/getDirMaterialList',
    params=params,
    headers=headers,
)
print(res.status_code)
print(res.text)


