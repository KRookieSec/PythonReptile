#coding:utf-8
#破解百度翻译,爬取单词对应的释义
#url是post请求（携带了参数），响应数据是一组json数据
import requests
import json
if __name__ == "__main__":
    #1、指定url
    post_url = 'https://fanyi.baidu.com/sug'
    #2、进行UA伪装
    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }
    #3、post请求处理参数（同get请求一致)
    word = input('请输入一个关键词：\n')
    data = {
        'kw':word
    }
    #4、请求发送
    response = requests.post(url=post_url,data=data,headers=headers)
    #5、获取响应数据,json()方法返回的是obj（若确认服务器响应数据是json类型的才可以使用json()
    dic_obj = response.json()
    #6、持久化存储
    filename = 'words'+'.json'
    with open(filename,'a+',encoding='utf-8') as fp:
        #fp.write('{}\n'.format())，在文件末尾加上换行符
        fp.write('{}\n'.format(json.dump(dic_obj,fp=fp,ensure_ascii=False)))
        fp.close
    print('Reptile over!')