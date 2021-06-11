#coding:utf-8
#双重m3u8，复杂视频爬取，以www.pianba.net为例，爬取越狱
#url = https://www.pianba.net/yun/25456-3-1.html
#m3u8_url = https://v2.dious.cc/20200901/CTiSO3VN/1000kb/hls/index.m3u8
#iframe src="https://jx.m3u8.tv/jiexi/?url=https://v2.dious.cc/20200901/CTiSO3VN/index.m3u8" 
'''
思路
    1、拿到主页面的页面源代码，找到iframe
    2、从iframe的页面源代码中拿到m3u8文件
    3、下载第一层m3u8文件 -> 下载第二层m3u8（视频存放路径）
    4、下载视频
    5、下载密钥，进行解密操作
    6、合并所有ts文件为一个mp4视频
'''
import requests
import re
from lxml import etree

#获取iframe，拿到m3u8文件
def get_iframe_src(url):
    resp = requests.get(url)
    #print(resp.text)
    #使用xpath解析页面
    html = etree.HTML(resp.text)
    #获取m3u8链接所在的标签内容，获得的结果为一个列表
    iframe = html.xpath("/html/body/div[1]/div/div/div/div/div[1]/div[1]/script[1]/text()")
    #将列表转换为字符串
    iframe_src = iframe[0]
    #去除字符串中的转义符\
    src_string = iframe_src.replace('\\','')
    #提取m3u8链接，获得的结果为列表
    src_list1 = re.findall(r'(https?://[^\s]+)","url_next',src_string)
    src_list2 = re.findall(r'"url_next":"(https?://[^\s]+)","from',src_string)
    #将列表转为字符串,得到m3u8链接
    src1 = src_list1[0]
    src2 = src_list2[0]
    print(src1)
    print(src2)

def main(url):
    #1、拿到主页面的页面源代码，找到iframe
    iframe_url = get_iframe_src(url)

if __name__ == "__main__":
    url = "https://www.pianba.net/yun/25456-3-1.html"
    main(url)
