#coding:utf-8
'''
    拿到页面源代码
    提取和解析数据
'''
import requests
from lxml import etree

url = "https://www.zbj.com/search/f/?type=new&kw=saas"
resp = requests.get(url)
#print(resp.text)

#解析
html = etree.HTML(resp.text)

#拿到每一个服务商的div
divs = html.xpath("/html/body/div[6]/div/div/div[2]/div[6]/div[1]/div")
print('------------------------------------------------------------------')
for div in divs:  #每一个服务商的信息
    img = "".join(div.xpath("./div/div/a[1]/div[1]/div[1]/div[1]/div[2]/img/text()"))
    price = "".join(div.xpath("./div/div/a[1]/div[2]/div[1]/span[1]/text()"))
    title = "saas".join(div.xpath("./div/div/a[1]/div[2]/div[2]/p/text()"))
    company = "".join(div.xpath("./div/div/a[2]/div[1]/p/text()"))
    local = "".join(div.xpath("./div/div/a[2]/div[1]/div/span/text()"))
    print(img)
    print(price)
    print(title)
    print(company)
    print(local)
    print('------------------------------------------------------------------')