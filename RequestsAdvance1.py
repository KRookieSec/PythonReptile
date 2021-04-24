#coding:utf-8
'''
登录 -> 得到cookie
带着cookie去请求到书架url -> 书架上的内容
必须把以上两个操作连起来
我们可以使用session进行请求 -> session可以认为是一连串的请求，在这个过程中cookie不会丢失
'''
import requests
#会话
session = requests.session()
data = {
    "loginName": "18673487039",
    "password": "xsp4436283"
}
header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"
}
#1、登录
url = "https://passport.17k.com/ck/user/login"
#发起一个会话
resp1 = session.post(url,data=data,headers=header)
""" print(resp1.text)
print('-------------------------')
print(resp1.cookies) #看cookie"""
#2、拿书架上的数据
#前面发起的session是有cookie的
resp2 = session.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919")
print(resp2.json())
