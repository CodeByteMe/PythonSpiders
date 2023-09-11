import requests
# 查看url地址及返回报文结构

# url="http://www.xinfadi.com.cn/getPriceData.html"
url="http://xinfadi.com.cn:8098/getPriceData.html"
# 请求参数构造
reqData={
    "limit": 500,
    "current": 1,
    "pubDateStartTime": "",
    "pubDateEndTime": "",
    "prodPcatid": "",
    "prodCatid": "",
    "prodName": ""
}
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

resp=requests.post(url,headers=headers,data=reqData)
print(resp.json())