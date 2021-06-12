#coding:utf-8
#使用selenium重新爬取越狱视频
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time
web = Chrome()
#如果页面中遇到了iframe如何处理
web.get("https://www.pianba.net/yun/25456-3-1.html")
#处理iframe必须先拿到iframe，然后切换视角到iframe，才可以拿数据
iframe = web.find_element_by_xpath('//*[@id="WANG"]')
#切换到iframe
web.switch_to.frame(iframe)
#切换回原页面
web.switch_to.default_content()
#获取iframe下的src属性
iframe_url = web.find_element_by_xpath('//*[@id="WANG"]/@src')
print(iframe_url)