#coding:utf-8
#线程池实战，抓取北京新发地菜价
'''
1、如何提取单个页面的数据
2、上线程池，多个页面同时抓取
'''
import requests
from lxml import etree   #使用xpath解析页面数据
import csv    #导入csv
from concurrent.futures import ThreadPoolExecutor   #导入线程池

f = open("data.csv", mode="w", encoding="utf-8")
csvwriter = csv.writer(f)

def download_one_oage(url):
    #拿到页面源代码
    resp = requests.get(url)
    html = etree.HTML(resp.text)
    #使用xpath解析页面数据，从网站页面中提取xpath
    table = html.xpath("/html/body/div[2]/div[4]/div[1]/table")[0]
    #拿到table下的所有tr
    trs = table.xpath("./tr")
    '''
    如果想要从第二个tr开始，可如下做
    1、trs = table.xpath("./tr")[1:]
    2、trs = table.xpath("./tr[position()>1]")
    '''
    #拿到每个tr
    for tr in trs:
        #拿到每个tr中的位于td下的文本数据
        TextData = tr.xpath("./td/text()")
        #对数据做简单的处理，去掉\\和/
        TextData = (item.replace("\\","").replace("/","")for item in TextData)
        #将数据写入csv文件
        csvwriter.writerow(TextData)
    print(url,"提取完毕！")

if __name__ == '__main__':
    '''
    单循环直接提取所有页面数据，效率极其低下
    for i in range(1,14870):
        download_one_oage(f"http://www.xinfadi.com.cn/marketanalysis/0/list/{i}.shtml")
    '''
    #创建有50个线程的线程池，使用线程提取页面数据
    with ThreadPoolExecutor(50) as t:
        #每个线程提取199页
        for i in range(200):
            #将下载任务提交给线程池
            t.submit(download_one_oage, f"http://www.xinfadi.com.cn/marketanalysis/0/list/{i}.shtml")
    print("全部下载完毕！")