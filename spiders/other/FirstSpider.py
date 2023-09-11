#导入url 浏览器模块儿
from urllib.request import urlopen
url="http://www.baidu.com"

resp=urlopen(url)

# print(resp.read().decode("utf-8"))

with open("baidu.html",mode="w",encoding="utf-8") as f:
    f.write(resp.read().decode("utf-8"))