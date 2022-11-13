# -*- coding: utf-8 -*-
from distutils.dir_util import copy_tree
from email import header
import requests
from bs4 import BeautifulSoup
import time

url = "https://www.xxx.com"
header = {
    "cookie": "xxxx",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}
try:
    resp = requests.get(url=url,headers=header)
    #print(resp.text)
    MainHtml = BeautifulSoup(resp.text,"html.parser")
    #所有页面DIV
    PageList = MainHtml.find("ol",class_="m-pagination").find_all("a",class_="m-pagination__item__link")
    #拿到所有页面的URL
    for i in range(0,11):
        if i == 1:
            PageURL = url + "/#pager"
            #print(PageURL)
        else:
            PageURL = url + str(i) + "/#pager"
        #print(PageURL)
        #请求所有页面
        PageResp = requests.get(url=PageURL,headers=header)
        PageHtml = BeautifulSoup(PageResp.text,"html.parser")
        #获取所有文章的URL
        ArticleList = PageHtml.find_all("div",class_="o-layout-list__item l-m-100 l-t-50 l-d-33")
        for Alist in ArticleList:
            ArticleURL = "https://www.xxx.com" + Alist.find("a")["href"]
            print(ArticleURL)
            #请求文章页面，获取文章标题、时间和正文
            ArticleResp = requests.get(url=ArticleURL,headers=header)
            ArticleHtml = BeautifulSoup(ArticleResp.text,"html.parser")
            ArticleTitle = ArticleHtml.find("h1",class_="t-content__title a-page-title").text
            ArticleTime = ArticleHtml.find("time").text
            ArticleContent = ArticleHtml.find("div",class_="t-content__body u-clearfix").find("p").text

            #.find_all("p").text
            filename = str(ArticleTitle) + ".txt"
            with open(filename,'a+',encoding='utf-8') as fp:
                fp.write(ArticleTitle)
                fp.write("\n")
                fp.write("时间：" + ArticleTime)
                fp.write("\n")
                fp.write(ArticleContent)
                fp.write("\n")
            fp.close()
            time.sleep(1)
except:
    print("error")
