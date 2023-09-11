import requests
from bs4 import BeautifulSoup
# 查看url地址及返回报文结构

# url="http://www.xinfadi.com.cn/getPriceData.html"
# url="http://xinfadi.com.cn:8098/minipricedetail.html"
url="http://www.xinfadi.com.cn/index.html"
resp=requests.get(url)
html=resp.text
# print(html)
# 创建BeautifulSoup4解析器
page=BeautifulSoup(html,"html.parser")
# page=BeautifulSoup(html,"lxml")
# print(page.prettify())
table=page.find("tbody")
print(table.text)