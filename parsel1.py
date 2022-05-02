#-*- coding: utf-8 -*-
import parsel
import requests
from urllib import request
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#去除InsecureRequestWarning

url = "https://freedomsecurityhacker.com"
resp = requests.get(url=url, verify=False)
sel = parsel.Selector(resp.content.decode("utf-8"))
li = sel.xpath('//*[@id="app-main"]/div[2]/div')
site_title = li.xpath('//*[@id="app-main"]/div[2]/div[4]/h1/text()').extract_first()
print(site_title)
i = 1
for list in li:
    title = list.xpath('//*[@id="app-main"]/div[2]/div[6]/div[1]/h3/a[2]/text()').extract_first()
    i = i + 1
    print(title)
