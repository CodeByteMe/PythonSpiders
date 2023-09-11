import re

# 直接拿到结果 列表形式的结果
re.findall(r"\d+","我是小学生，今年5岁了")
# 迭代器拿到迭代器对象，然后通过for循环进行打印 item.group()
re.finditer(r"\d+","我是小学生，今年5岁了")
# 循环到一次就返回
re.search(r"\d+","我是小学生，今年5岁了")


# 预加载 提前加载正则表达式
obj=re.compile(r"\d+")
obj.findall("我是孔明明123来来来")




