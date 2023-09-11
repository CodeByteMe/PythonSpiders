import requests
content=input('请输入单词')
url="https://fanyi.baidu.com/sug"
reqData={
    "kw":{content}
}
resp=requests.post(url,data=reqData)

json=resp.json()
print(json)

