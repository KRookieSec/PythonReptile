#coding:utf-8
#处理12306登录问题
from selenium.webdriver import Chrome
from chaojiying import Chaojiying_Client
from selenium.webdriver.chrome.options import Options
#事件链
from selenium.webdriver.common.action_chains import ActionChains
import time

#初始化超级鹰
chaojiying = Chaojiying_Client('TheSky', 'XSP4436283asd,', '918349')
'''
如果网站识别到了浏览器是被自动化测试工具控制的怎么办
1、如果chrome版本小于88
在启动浏览器时（此时没有加载任何网页内容），向页面嵌入js代码，去掉webdriver
web = Chrome()
web.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",{
    "source":"""
    window.navigator.webdriver = undefined
        Object.defineProperty(navigator,'webdriver',{
            get:() => undefined
        })
    """
})

2、如果chrome版本大于88
option = Options()
option.add_argument('--disable-blink-features=AutomationControlled')
web = Chrome(option=option)
'''
option = Options()
option.add_argument('--disable-blink-features=AutomationControlled')
web = Chrome(options=option)

web.get('https://kyfw.12306.cn/otn/resources/login.html')
time.sleep(3)

#切换到账号登陆
web.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a').click()
time.sleep(4)
#先处理验证码
verify_img_element = web.find_element_by_xpath('//*[@id="J-loginImg"]')

#用超级鹰识别验证码
dic = chaojiying.PostPic(verify_img_element.screenshot_as_png, 9004)
#返回验证码结果坐标
result = dic['pic_str']
#print(result)
#处理坐标
#以|做切割
rs_list = result.split("|")
for rs in rs_list:
    #以,做切割
    p_temp = rs.split(",")
    #将处理后得到的字符串形式的坐标转化为数字
    x = int(p_temp[0])
    y = int(p_temp[1])
    #让鼠标移动到某一个位置，然后进行点击
    #以验证码所在区块顶点为节点，进行偏移量移动
    ActionChains(web).move_to_element_with_offset(verify_img_element,x,y).click().perform()  

#输入用户名和密码
web.find_element_by_xpath('//*[@id="J-userName"]').send_keys("18673487039")
web.find_element_by_xpath('//*[@id="J-password"]').send_keys("xsp4436283")

#点击登录
web.find_element_by_xpath('//*[@id="J-login"]').click()
time.sleep(5)
#拖拽验证进度条
btn = web.find_element_by_xpath('//*[@id="nc_1_n1z"]')
ActionChains(web).drag_and_drop_by_offset(btn,300,0).perform()
