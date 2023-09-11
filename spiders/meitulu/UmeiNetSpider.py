import requests
from bs4 import BeautifulSoup

# 定义domain
domain="https://umei.net"
# 定义一个url
# url="https://umei.net/tags/jk/"
# url="https://umei.net/tags/ribenzhifu/"
url="https://umei.net/e/search/result/?searchid=3010"
"""
    注意：
        1.当获取href时, 子页面链接带/ 那么直接拼接上domain即可
        2.当获取href时, 子页面链接不带/ 那么链接要拼上当前页最后一个/为结尾的前缀的链接
"""

img_set=set()

def childIteratorDownloadImgs(url):
    try:
        print("抓取url:%s"%url)
        global img_set
        #请求子页面url
        child_resp=requests.get(url)
        child_resp.encoding="utf-8"
        child_html=child_resp.text
        # 子页面html解析
        child_page=BeautifulSoup(child_html,"html.parser")
        child_div=child_page.find("div",attrs={"class":"image_div"})
        child_img=child_div.find("img")
        if child_img is None:
            print("没有图片，跳过不处理")
            pass
        else:
            imgUrl=child_img.get("src")
            print("图片地址：%s"%imgUrl)
            img_set.add(imgUrl)
            ul_page=child_page.find("ul",attrs={"class":"page"})
            ul_page_nth_li=ul_page.select("li:nth-last-child(1)")
            next_url_li=ul_page_nth_li[0]
            next_a=next_url_li.find("a")
            next_a_href=next_a.get("href")
            if next_a_href is None:
                print("没有下一页数据... ...")
                pass
            else:
                next_href=domain+next_a_href
                childIteratorDownloadImgs(next_href)
    except Exception:
        print("异常跳过... ...")

# 下载图片
def download(imgSrcUrl,fileName):
    try:
        imgResp=requests.get(imgSrcUrl)
        with open(f"../imgs/{fileName}.jpg",mode="wb") as f:
            f.write(imgResp.content)
    except Exception:
        print("下载链接超时，跳过不处理... ...")


# main
resp=requests.get(url)
resp.encoding="utf-8"
html=resp.text
page=BeautifulSoup(html,"html.parser")
li_list=page.find_all("li",attrs={"class":"i_list list_n2"})
for li in li_list:
    a=li.find("a")
    href=a.get("href")
    child_url=domain+href
    childIteratorDownloadImgs(child_url)

# 判断图片 并下载
n=1
if img_set is not None:
    for imgsrc in img_set:
        fileName="img"+str(n)
        print("正在下载图片:%s"%fileName)
        download(imgsrc,fileName)
        n+=1

print("下载完毕... ...")