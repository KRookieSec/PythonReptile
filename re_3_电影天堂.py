#codind:utf-8
#爬取电影天堂电影的下载地址
#定位到2021年必看片；
#从2021年必看片中提取到子页面的链接地址
#请求子页面的链接地址，拿到想要的下载地址
import requests
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#1、指定url
domain = "https://dytt89.com/"
#2、UA伪装
header = {
    "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
}
#3、发送请求
resp = requests.get(domain,headers=header,verify=False)   #verify=False去掉安全验证
resp.encoding = 'gb2312'    #指定字符集
#print(resp.text)
#拿到ul里面的li(电影简介)
obj1 = re.compile(r"2021必看热片.*?<ul>(?P<ul>.*?)</ul>", re.S)
#拿到电影子页面的地址
obj2 = re.compile(r"<a href='(?P<href>.*?)'",re.S)
#拿到子页面中电影的下载地址
obj3 = re.compile(r'◎片　　名(?P<movie>.*?)<br />.*? <td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">',re.S)
#4、获取响应数据
result1 = obj1.finditer(resp.text)
child_href_list = []
for it in result1:
    ul = it.group('ul')
    #print(ul)
    #提取子页面链接
    result2 = obj2.finditer(ul)
    for itt in result2:
        #拼接子页面的url地址：域名+子页面地址
        child_href = domain + itt.group('href').strip()
        #print(child_href)
        #把子页面链接保存到列表中
        child_href_list.append(child_href)
#5、提取子页面内容,持久化存储
filename = '电影天堂2021必看片'+'.txt'
for href in child_href_list:
    child_resp = requests.get(href,headers=header,verify = False)
    child_resp.encoding = 'gb2312'
    result3 = obj3.search(child_resp.text)
    #print(result3.group("movie")+"下载地址：\n"+result3.group("download"))
    with open(filename,'a+',encoding='utf-8') as fp:
        fp.write('{}\n'.format(result3.group("movie")+"下载地址："+result3.group("download")))
fp.close
print("Reptile over!")

