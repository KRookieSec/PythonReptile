#coding:utf-8
#网页采集器
#User-Agent(请求载体的身份标识)
'''
UA检测：门户网站的服务器会检测对应请求的载体的身份标识，
若检测到请求的载体身份标识为某一款浏览器，说明该请求是一个正常的请求，
若检测到请求的载体身份标识不是某一款浏览器的，则表示该请求为不正常的请求,
服务器端可能拒绝该次请求
'''
'''
UA伪装：让爬虫对应的请求载体身份标识伪装成某一款浏览器
'''
import requests
if __name__ == "__main__":
    #UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }
    #1、指定url
    url = 'https://sogou.com/web'
    #处理url携带的参数：封装到字典中，通过输入关键字搜索指定页面
    kw = input('输入一个关键字：\n')
    param = {
        'query':kw
    }
    #2、发起请求，对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url,params=param,headers=headers)
    #3、获取响应数据
    page_text = response.text
    #4、持久化存储,将获取到的数据保存到指定文件中
    filename = kw+'.html'
    with open(filename,'a',encoding='utf-8') as fp:
        fp.write(page_text)
        fp.close
    print(filename,'保存成功！')