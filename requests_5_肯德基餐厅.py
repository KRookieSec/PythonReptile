#coding:utf-8
#爬取肯德基餐厅数据
import requests
import json


#1、指定url
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
#2、UA伪装
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}
#3、配置url参数
ke = input('请输入地区：')
data = {
   'cname': '',
   'pid': '',
   'keyword': ke,
   'pageIndex': '1',
   'pageSize': '10',
}
#4、请求发送
response = requests.post(url=url,data=data,headers=headers)
#5、获取响应数据
page = response.json()
#6、持久化存储，保存爬取的数据
filename = 'KFC'+'.json'
with open(filename,'a+',encoding='utf-8') as fp:
    fp.write('{}\n'.format(json.dump(page,fp=fp,ensure_ascii=False)))
    fp.close
print('Reptile over!')