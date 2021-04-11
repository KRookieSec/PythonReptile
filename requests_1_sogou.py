#coding:utf-8
#requetst模块
#一、爬取搜狗首页的页面数据
import requests
if __name__ == "__main__":
    #1、指定url
    url = 'https://sogou.com/'
    #2、发起请求
    #使用requests模块的get()方法,get()会返回一个响应对象
    response = requests.get(url=url)
    #3、获取响应数据，text返回的是字符串形式的响应数据
    page_text = response.text
    print(page_text)
    #4、持久化存储
    with open('./sogou.html','a',encoding='utf-8') as fp:
        fp.write(page_text)
        fp.close
    print('爬取结束！')