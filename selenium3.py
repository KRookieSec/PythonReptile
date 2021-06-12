#coding:utf-8
#使用selenium进行窗口之间的切换
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time
web = Chrome()
web.get("http://lagou.com")
#找到x链接，点击它
web.find_element_by_xpath('//*[@id="cboxClose"]').click()
time.sleep(1)
#搜索关键词
web.find_element_by_xpath('//*[@id="search_input"]').send_keys("python",Keys.ENTER)
time.sleep(1)
#定位到关键词的详情页链接,点击它
web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a/h3').click()
#如何进入到新窗口中进行提取，在selenium中，新窗口默认是不切换过来的
#将视角调整到新窗口，新窗口放到最后
web.switch_to.window(web.window_handles[-1])
#在新窗口中提取内容
job_detail = web.find_element_by_xpath('//*[@id="job_detail"]/dd[2]/div').text
print(job_detail)
#关闭当子前窗口
web.close()
#将视角重新调整为之前的窗口
web.switch_to.window(web.window_handles[0])
print(web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a/h3').text)
