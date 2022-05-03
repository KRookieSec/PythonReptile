#-*- coding: utf-8 -*-
import parsel
import requests
from urllib import request, response
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://freedomsecurityhacker.com"
resp = requests.get(url=url, verify=False)
#parsel解析网站数据
sel = parsel.Selector(resp.content.decode("utf-8"))
#定位到页面主体区域
li = sel.xpath('//*[@id="app-main"]/div[2]/div')
#获取网站标题
site_title = li.xpath('//*[@id="app-main"]/div[2]/div[4]/h1/text()').extract_first()
#print(site_title)
#获取网站底部page的最大数字，即最后一个页面的ID
pagelink_list_num = li.xpath('//*[@id="app-main"]/div[2]/ol//a/text()').extract()[-1]
#获取第一个页面的URL，用来做切片，拼接全部页面的URL
pagelink_list_url = li.xpath('//*[@id="app-main"]/div[2]/ol//a/@href').extract()[0]
#print(pagelink_list_url)
#拼接获取网站所有page页面URL
for item in range(1,int(pagelink_list_num)+1):
    #当前页面的URL
    pagelink = pagelink_list_url[0:-2] + str(item)
    #print(pagelink)
    #请求当前页面
    pageresp = requests.get(url = pagelink,verify=False)
    #指定编码，防止中文乱码
    pageresp.encoding='GBK'
    pageresp.encoding='utf-8'
    #解析当前页面
    newsel = parsel.Selector(pageresp.content.decode("utf-8"))
    #定位到当前页面的主体区域
    newli = newsel.xpath('//*[@id="app-main"]/div[2]/div[6]/div')
    i = 1
    #获取当前页面的文章标题和URL
    for list in newli:
        #获取文章标题
        title = list.xpath('//*[@id="app-main"]/div[2]/div[6]/div['+ str(i) +']/h3/a[2]/text()').extract_first()
        #获取文章URL
        article_url = list.xpath('//*[@id="app-main"]/div[2]/div[6]/div['+ str(i) + ']/h3/a[2]/@href').extract_first()
        i = i + 1
        """ print(title)
        print(article_url) """
        #请求到当前文章
        articleresp = requests.get(url=article_url,verify=False)
        articlesel = parsel.Selector(articleresp.content.decode("utf-8"))
        #指定编码，防止中文乱码
        articleresp.encoding='GBK'
        articleresp.encoding='utf-8'
        #定位到当前文章的正文区域
        current_article_content = articlesel.xpath('//*[@id="write"]//text()').extract()
        #print(current_article_content)
        #去除文章标题中的换行和空格
        article_title = title.replace('\n','').replace(' ','')
        #给每个段落增加换行
        article_content = ''
        for j in current_article_content:
            article_content = article_content + j.strip()+'\r\n'
        #将文章标题、URL、正文存储到本地文件中，注意，with open里面必须指定编码打开文件，否则可能出现中文乱码
        with open(f"{article_title}.md",'w',encoding='utf-8') as file:
            file.write(article_title)
            file.write("\n")
            file.write(article_url)
            file.write("\n")
            file.write(str(article_content))
            file.close()
