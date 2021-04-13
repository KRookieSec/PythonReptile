#coding:utf-8
#爬取国家药品药品监督管理局化妆品企业许可证
import requests
import json
#批量获取不同企业的id值
'''
检查网站子页面后发现，url值都相同，只有携带的参数不同，即ID值不同，
观察后发现，化妆品主页面能够获取到不同公司许可证的ID值，通过ID值能够获取到各个公司许可证的详情
'''
url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
#参数的封装
data = {
    'on': 'true',
    'page': '1',
    'pageSize': '15',
    'productName': '',
    'conditionType': '1',
    'applyname':'',
    }
#UA伪装
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}
#请求发送,获取响应数据
id_list = []    #存储企业的id
company_list = []   #存储企业详情数据
json_ids = requests.post(url=url,data=data,headers=headers).json()
'''
从化妆品主页面获取到的数据为一个字典，ID值存储在list键中
遍历该字典获取ID值并封装到列表中
'''
for dic in json_ids['list']:
    id_list.append(dic['ID'])
print(id_list)
#获取企业详情数据
#企业详情数据的url

Company_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
#遍历ID值列表，配置企业详情数据url的参数
for id in id_list:
    Company_data = {
        'id':id
    }
    #发送请求并获取响应数据
    detail_json = requests.post(url=Company_url,data=Company_data,headers=headers).json()
    company_list.append(detail_json)
#持久化存储企业详情数据
filename = '药监局'+'.json'
with open(filename,'a+',encoding='utf-8') as fp:
    fp.write('{}\n'.format(json.dump(company_list,fp=fp,ensure_ascii=False)))
    fp.close
print('Reptile over!')