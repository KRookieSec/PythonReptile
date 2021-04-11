#coding:utf-8
#豆瓣电影爬取
import requests
import json
if __name__ == "__main__":
    #1、指定url
    url = 'https://movie.douban.com/j/chart/top_list'
    #2、配置url携带的参数
    param = {
        'type': '20',
        'interval_id': '100:90',
        'action':'', 
        'start': '1',        #从库中的第几部电影去取
        'limit': '20',       #一次取出多少部
    }
    #3、进行UA伪装
    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }
    #4、请求发送
    response = requests.get(url=url,params=param,headers=headers)
    #5、获取响应数据
    list_data = response.json()
    #6、持久化存储
    filename = '豆瓣电影'+'.json'
    with open(filename,'a+',encoding='utf-8') as fp:
        fp.write('{}\n'.format(json.dump(list_data,fp=fp,ensure_ascii=False)))
        fp.close
    print('Reptile over!')