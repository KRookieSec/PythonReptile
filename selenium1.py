#coding:utf-8
#selenium模块，自动化测试工具
#可以打开浏览器，然后像人一样去操作浏览器
#可以从selenium中提取网页上的各种信息
'''
环境搭建
    pip install selenium
    下载浏览器驱动：https://npm.taobao.org/mirrors/chromedriver
    根据瀏覽器版本選擇驅動版本，若無對應版本，則往回找最近的版本
    把解压缩的浏览器驱动放在python解释器所在的文件夹

#让selenium启动谷歌浏览器
from selenium.webdriver import Chrome

#1、创建浏览器对象
web = Chrome()
#2、打开一个网址
web.get(url)
'''
from selenium.webdriver import Chrome
#1、创建浏览器对象
web = Chrome()
#2、打开一个网址
url = "http://www.bilibili.com"
web.get(url)
print(web.title)
web.close()
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager(version="93.0.4535.2").install())
# driver.get("https://www.google.com")