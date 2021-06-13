#coding:utf-8
#无头浏览器
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
#定位到年份下拉列表
sel_el = web.find_element_by_xpath('//*[@id="OptionDate"]')
#对元素进行包装，包装成下拉菜单
sel = Select(sel_el)
#让浏览器进行调整选项
for i in range(len(sel.options)):  #i就是每一个下拉框选项的索引位置
    sel.select_by_index(i)  #按照索引进行切换
    time.sleep(2)
    #定位到所有数据
    table = web.find_element_by_xpath('/html/body/section[1]/div/div[2]/div/div')
    print(table.text)  #打印所有文本信息
    print('==============================================')
print("运行完毕。")
web.close()

