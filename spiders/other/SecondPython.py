import requests
content=input('请输入搜索关键字')
url=f"https://www.sogou.com/web?query={content}"
headers={
    # 添加一个请求头信息，用于处理反爬机制
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}
resp=requests.get(url,headers=headers)
# print(resp.text)

print(resp.request.headers)