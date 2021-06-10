#coding:utf-8
#从91看剧网站爬取的视频，简单爬取，不使用线程、协程
'''
流程
    1、拿到54812-1-1.html的页面源代码
    2、从源代码中提取到m3u8的url
    3、下载m3u8
    4、读取m3u8文件，下载视频
    5、合并视频
'''
import requests
import re   #使用正则解析源码
#UA伪装
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4530.3 Safari/537.36"
}
#解析网页源代码，提取m3u8的地址
obj = re.compile(r"url: '(?P<url>.*?)',",re.S)
#网站url
url = "https://www.91kanju.com/vod-play/54812-1-1.html"
#发送请求
resp = requests.get(url,headers=headers)
#print(resp.text)
#拿到m3u8的地址
m3u8_url = obj.search(resp.text).group("url")
#print(m3u8_url)
resp.close()
#下载m3u8文件
resp2 = requests.get(m3u8_url,headers=headers)
with open("哲仁王后.m3u8",mode="wb") as f:
    f.write(resp2.content)
resp2.close()
print("下载完毕！")

#解析m3u8文件
n = 1
with open("哲仁王后.m3u8",mode="r",encoding="utf-8") as fp:
    #逐行读取m3u8文件
    for line in fp:
        #先去掉空格、空白、换行符
        line = line.strip()
        #如果以#开头则不要
        if line.startswith("#"):
            continue
        #下载视频片段
        resp3 = requests.get(line)
        fp = open(f"easy_video/{n}.ts",mode="wb")
        fp.write(resp3.content)
        fp.close()
        resp3.close()
        print(f"完成了{n}个。")
        n += 1