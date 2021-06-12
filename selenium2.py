#coding:utf-8
#selenium的各種操作
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys   #使用各种按键
import time
web = Chrome()
web.get("http://lagou.com")
#找到某个元素，点击它
el = web.find_element_by_xpath('//*[@id="changeCityBox"]/p[1]/a')
#点击事件
el.click()
time.sleep(1)
#找到输入框，输入python => 输入回车/点击搜索按钮
web.find_element_by_xpath('//*[@id="search_input"]').send_keys("python",Keys.ENTER)
time.sleep(1)
#查找存放数据的位置，进行数据提取
#找到页面中存放数据的所有li
li_list = web.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li')
for li in li_list:
    job_name = li.find_element_by_tag_name("h3").text
    job_price = li.find_element_by_xpath('./div/div/div[2]/div/span').text
    job_local = li.find_element_by_xpath('./div/div/div[1]/a/span/em').text
    job_company = li.find_element_by_xpath('./div[1]/div[2]/div[1]/a').text
    job_product = li.find_element_by_xpath('./div[1]/div[2]/div[2]').text
    print(f"类型：{job_name},工资：{job_price},地点：{job_local}，公司名称：{job_company}，产品与规模：{job_product}")