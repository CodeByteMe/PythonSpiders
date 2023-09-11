import requests
import threading
import re


# 1.分析电影天堂网页结构
baseUrl="https://www.dy2018.com"
firstUrl=baseUrl+"/html/bikan/index.html"
detailList=[]
afterFlag=False

# 定义一个递归函数
def iteratorSpider(url):
    global afterFlag,detailList
    # 声明request对象
    resp=requests.get(url)
    resp.encoding='gbk'
    htmlContent=resp.text
    # 抓取第一页爬虫书写正则 拿到指定列表
    firstReObj=re.compile(r'<div class="co_content8">.*?<ul>(?P<html>.*?)</ul>',re.S)
    result=firstReObj.search(htmlContent)
    html=result.group('html')
    # 寻找带有电影链接的url
    hrefReObj=re.compile(r'<b>.*?<a href="(?P<hrefLink>.*?)" class="ulink" title=.*?</b>',re.S)
    # 循环列表
    hrefList=hrefReObj.finditer(html)
    for item in hrefList:
        href=item.group('hrefLink')
        # 获取分页数据连接
        detail_url=baseUrl+href
        detailList.append(detail_url)
    # 当前页数据读取完毕

    # 抓取下一页链接
    nextUrlObj=re.compile(r"上一页.*?<a href='(?P<nextPageUrl>.*?)'>下一页</a>",re.S)
    # 查找页面元素
    nextPageUrlResult=nextUrlObj.search(htmlContent)
    if nextPageUrlResult is None:
        print("没有下一页数据....爬虫结束...")
        afterFlag=True
        pass
    else:
         # 取值下一页link url
        nextPageUrl=nextPageUrlResult.group('nextPageUrl')
        if nextPageUrl is None:
            print("没有下一页数据....爬虫结束...")
            afterFlag=True
            pass
        else:
             thisUrl=baseUrl+nextPageUrl
             iteratorSpider(thisUrl)



# 抓取详情
def crawl(url):
    print("正在提取 (%s) 页面数据... ..."%url)
    detailResp=requests.get(url)
    detailResp.encoding='gbk'
    detailHtml=detailResp.text


    # 解析网页数据
    detailReObj=re.compile(r'<div id="Zoom">.*?◎译　　名(?P<enName>.*?)<br />'
                           r'.*?◎片　　名(?P<name>.*?)<br />.*?◎简　　介<br />(?P<desc>.*?)<br />'
                           r'.*?◎影片截图<br /><img alt="" src="(?P<img>.*?)" style'
                           r'.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<downloadLink>.*?)"'
                           ,re.S)
    detailRes=detailReObj.search(detailHtml)
    enName=detailRes.group('enName')
    name=detailRes.group('name')
    img=detailRes.group('img')
    desc=detailRes.group('desc')
    downloadLink=detailRes.group('downloadLink')
    print("英文名：%s"%enName,"\r\n片名：%s"%name,"\r\n截图：%s"%img,"\r\n下载链接：%s"%downloadLink,"\r\n影片描述：%s"%desc)
    print("===================================================================================================================================================")


#多线程爬取数据
def threadSpider(urlList):
    # 定义多线程进行爬取数据
    threads = []
    # 创建多线程数组
    for url in urlList:
        t = threading.Thread(target=crawl,args=(url,))
        t.start()
        threads.append(t)

    # 加入线程组遍历
    for t in threads:
        t.join()


# 函数调用 iteratorSpider
iteratorSpider(firstUrl)
# 详情数据抓取
if afterFlag:
    print(len(detailList))
    threadSpider(detailList)





# 根据url 提取页面元素

# 2.提取URL 并根据链接进行提取html 页面元素