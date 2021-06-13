#coding:utf-8
#无头浏览器
#如何拿到经过数据加载以及js执行后的结果的html内容的页面代码（Elements)
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time

#配置好参数，运行程序时不打开浏览器
opt = Options()
opt.add_argument('--headless')
opt.add_argument('--disable-gpu')  #不显示
#发起请求，将参数配置添加到浏览器中
web = Chrome(options=opt)  
web.get("https://www.endata.com.cn/BoxOffice/BO/Year/index.html")
#获取经过数据加载以及js执行后的结果的html内容的页面代码（Elements)
time.sleep(2)
print(web.page_source)