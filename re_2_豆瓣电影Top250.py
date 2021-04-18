#coding:utf-8
#爬虫正则实战，豆瓣电影Top250
import requests
import re
import csv
#1、指定url
url = "https://movie.douban.com/top250"
#2、UA伪装
header = {
    "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
}
#3、获取响应数据
resp = requests.get(url,headers=header)
page_content = resp.text
#4、使用正则解析数据
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<filmname>.*?)'
                 r'</span>.*?<span class="other">&nbsp;/&nbsp;(?P<othername>.*?)</span>.*?'
                 r'<p class="">(?P<director>.*?)&nbsp;&nbsp;&nbsp;(?P<actor>.*?)<br>'
                 r'(?P<year>.*?)&nbsp;/&nbsp;(?P<contry>.*?)&nbsp;/&nbsp;(?P<type>.*?)</p>.*?'
                 r'<div class="star">.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                 r'<span>(?P<Evaluation>.*?)</span>',re.S)
#5、开始匹配
result = obj.finditer(page_content)
#6、持久化存储
f = open("豆瓣电影Top250.csv",mode='a',encoding='utf-8')
csvwriter = csv.writer(f)
for it in result:
    '''
    print(it.group("filmname")+' / '+it.group("othername"))
    print(it.group("director").strip())
    print(it.group("actor"))
    print(it.group("year").strip()+' / '+it.group("contry")+' / '+it.group("type").strip())
    print(it.group("score").strip()+' / '+it.group("Evaluation"))
    print('\n')
    '''
    dic = it.groupdict()
    dic["director"] = dic["director"].strip()
    dic['year'] = dic['year'].strip()
    dic["type"] = dic["type"].strip()
    dic["score"] = dic["score"].strip()
    csvwriter.writerow(dic.values())
    
f.close()
print("Reptile over!")