import requests

url="https://movie.douban.com/j/chart/top_list"

req={
    "type":"13",
    "interval_id":"100:90",
    "action":"",
    "start":"0",
    "limit":"20"
}

headers={
    # 添加一个请求头信息，用于处理反爬机制
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

resp=requests.get(url,headers=headers,params=req)

print(resp.json())