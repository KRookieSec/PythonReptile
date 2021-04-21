#coding:utf-8
#爬取北京新发地大白菜菜价
#一、拿到页面源代码
#二、使用bs4进行解析，拿到数据
import requests
from bs4 import  BeautifulSoup
import csv
#配置url
url = "http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml"
resp = requests.get(url)
f = open("菜价.csv",mode="a+")
csvwrite = csv.writer(f)
#解析数据
#1、把页面源代码交给BeautifulSoup进行处理，生成bs对象
page = BeautifulSoup(resp.text,"html.parser")
#2、从bs对象中查找数据
#find(标签，属性=值)，查找一个对象
#find_all(标签，属性=值)，查找所有对象
#page.find("table",class_="hq_table")  #class是python的关键字为了区分，应在class后加下划线
table = page.find("table",attrs={"class":"hq_table"})   #和上一行一个意思，此时可以避免class问题
#拿到所有数据
trs = table.find_all("tr")    #对源代码中tr的内容作切片
for tr in trs:    #每一行
    tds = tr.find_all("td")  #拿到每行中的所有td
    name = tds[0].text       #.text表示拿到被标签标记的内容
    low = tds[1].text
    avg = tds[2].text
    high = tds[3].text
    gui = tds[4].text
    kind = tds[5].text
    data = tds[6].text
    csvwrite.writerow([name,low,avg,high,gui,kind,data])
f.close()
print("Reptile over!")