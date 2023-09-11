import re

htmlContent="""
    <div class='sub'><span id='10010'>中国联通</span></div>
    <div class='sub'><span id='10086'>中国移动</span></div>
"""

obj=re.compile(r"<span id='(?P<id>\d+)'>(?P<name>.*?)</span")
result=obj.finditer(htmlContent)

for ite in result:
    print(ite.group("id"))
    print(ite.group("name"))