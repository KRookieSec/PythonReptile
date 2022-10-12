# -*- coding: utf-8 -*-
from distutils.dir_util import copy_tree
from email import header
import requests
from bs4 import BeautifulSoup
import time

url = "https://www.rfi.fr/cn/%E4%BD%9C%E8%80%85/%E5%AE%89%E5%BE%B7%E7%83%88/"
header = {
    "cookie": "didomi_token=eyJ1c2VyX2lkIjoiMTgzY2JlMzMtN2I1MS02NTJlLWJlYTctNGEzMjZmYjc5NTc2IiwiY3JlYXRlZCI6IjIwMjItMTAtMTJUMTE6MTA6MTMuNjY5WiIsInVwZGF0ZWQiOiIyMDIyLTEwLTEyVDExOjEwOjEzLjY2OVoiLCJ2ZW5kb3JzIjp7ImRpc2FibGVkIjpbInR3aXR0ZXIiLCJnb29nbGUiLCJjOnZkb3BpYSIsImM6ZGlkb21pIiwiYzphZHZlcnRpc2luZ2NvbSIsImM6a3J1eC1kaWdpdGFsIiwiYzp5b3V0dWJlIiwiYzpob3RqYXIiLCJjOmluc3RhZ3JhbSIsImM6bmV3LXJlbGljIiwiYzpjaGFydGJlYXQiLCJjOnF1YW50dW0tYWR2ZXJ0aXNpbmciLCJjOnBpbmdkb20iLCJjOmF1ZGllbmNlLXNxdWFyZSIsImM6bGtxZCIsImM6b3ducGFnZSIsImM6c29hc3RhLW1wdWxzZSIsImM6YmF0Y2giLCJjOm5vbmxpIl19LCJ2ZXJzaW9uIjoyLCJhYyI6IkFBQUEuQUFBQSJ9; euconsent-v2=CPgvCMAPgvCMAAHABBENCkCgAAAAAAAAAAqIAAAAAAEkoAMAAQSIDQAYAAgkQKgAwABBIgpABgACCRA6ADAAEEiCEAGAAIJEBIAMAAQSIEQAYAAgkQMgAwABBIgA.YAAAAAAAAAAA; atuserid=%7B%22name%22%3A%22atuserid%22%2C%22val%22%3A%228461717e-093d-477e-8818-c91c4a06b288%22%2C%22options%22%3A%7B%22end%22%3A%222023-11-13T11%3A10%3A21.672Z%22%2C%22path%22%3A%22%2F%22%7D%7D; atauthority=%7B%22name%22%3A%22atauthority%22%2C%22val%22%3A%7B%22authority_name%22%3A%22cnil%22%2C%22visitor_mode%22%3A%22exempt%22%7D%2C%22options%22%3A%7B%22end%22%3A%222023-11-13T11%3A10%3A21.672Z%22%2C%22path%22%3A%22%2F%22%7D%7D; _tms_journey=%7B%22evt%22%3A%7B%22push_subscription%22%3A1%2C%22pwa_banner%22%3A0%2C%22app_banner%22%3A0%2C%22popinSurvey%22%3A1%7D%2C%22pagesRead%22%3A2%2C%22end%22%3A%22Wed%2C%2019%20Oct%202022%2011%3A10%3A09%20GMT%22%7D; nlbi_1314842=otHTTEh3+TM1Cfiqk8O1lQAAAAAhAGJRh+whZb6p1HzqxTub; visid_incap_1314842=Tuf29pItQ2++sTNAbjbzwt6fRmMAAAAAQUIPAAAAAACBPCHr+ZeSaC76IQx6H1Kh; incap_ses_536_1314842=vmpuDSpqtAnr6aqJ40FwB6WgRmMAAAAA0qcrYbvxDoYH2H65AQDvPw==",
    "dnt": "1",
    "referer": "https://www.rfi.fr/cn/service-worker?v=2.3.19",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
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
            ArticleURL = "https://www.rfi.fr" + Alist.find("a")["href"]
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
