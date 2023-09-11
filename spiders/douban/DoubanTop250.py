import requests
import re
# 分析网页结构
# 拿到请求url
url="https://movie.douban.com/top250"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

reqParams={
    "start":"0",
    "filter":""

}

f=open("top250.csv",mode="w",encoding="utf-8")

html=requests.get(url,headers=headers,params=reqParams)
# 拿到源码
text=html.text
print(text)
# 提取数据
obj=re.compile(r'<div class="item">.*?<span class="title">(?P<name>.*?)</s'
               r'pan>.*?<p class="">.*?导演: (?P<dao>.*?)&nbsp;.*?<br>'
               r'(?P<year>.*?)&nbsp;.*?<span class="rating_num" property="v:average">'
               r'(?P<score>.*?)</span>.*?<span>(?P<num>.*?)人评价</span>',re.S)
result=obj.finditer(text)
for item in result:
    print("电影：《%s》"%item.group('name')
          ,"\r\n导演：%s"%item.group('dao')
          ,"\r\n年份：%s"%item.group('year')
          ,"\r\n评价数：%s"%item.group('num')
          ,"\r\n评分：%s"%item.group('score'))
    print("==========================================================")
    # f.write(f"{item.group('name')},{item.group('dao')},{item.group('year')},{item.group('score')},{item.group('num')}\n")
# 保存数据
f.close()
html.close()