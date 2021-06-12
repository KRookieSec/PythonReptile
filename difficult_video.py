#coding:utf-8
#双重m3u8，复杂视频爬取，以www.pianba.net为例，爬取越狱
#url = https://www.pianba.net/yun/25456-3-1.html
#存放m3u8链接的js脚本链接https://www.pianba.net/static/js/playerconfig.js?t=20210611
#m3u8_url = https://v2.dious.cc/20200901/CTiSO3VN/1000kb/hls/index.m3u8
#iframe src="https://jx.m3u8.tv/jiexi/?url=https://v2.dious.cc/20200901/CTiSO3VN/index.m3u8" 
'''
思路
    1、拿到主页面的页面源代码，找到存放m3u8链接
    2、从页面源代码中拿到m3u8链接，拿到m3u8文件
    3、下载第一层m3u8文件 -> 下载第二层m3u8（视频存放路径）
    4、下载视频
    5、下载密钥，进行解密操作
    6、合并所有ts文件为一个mp4视频
'''
from asyncio import tasks
import requests
import re
from lxml import etree
import asyncio
import aiohttp
import aiofiles
from Crypto.Cipher import AES     #先安装Crypto,将python3安装目录下的Lib/sit-package下的crypto改为Crypto，再安装pycryptodome
import os
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)

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
    #将列表转为字符串,得到第一层m3u8链接下载地址
    src1 = src_list1[0]
    #src2 = src_list2[0]
    #print(src1)
    #print(src2)
    return src1

#下载m3u8文件
def download_m3u8_file(url,name):
    resp = requests.get(url)
    with open(f"越狱/{name}",mode='wb') as f:
        f.write(resp.content)

#异步协程下载ts视频
async def download_ts(url,name,session):
    async with session.get(url) as resp:
        async with aiofiles.open(f"越狱/video/{name}",mode='wb') as f:
            #把下载的内容写入文件
            await f.write(await resp.content.read())
    print(f"下载{name}完毕。")

#异步协程下载视频
async def aio_download(url):
    tasks = []
    url_name = []
    async with aiohttp.ClientSession() as session:
        async with aiofiles.open(f"越狱/越狱第一季第一集_second_m3u8.txt",mode="r",encoding="utf-8") as f:
            async for line in f:
                #如果以#开头则舍弃
                if line.startswith("#"):
                    continue
                #去掉空格和换行符
                line = line.strip()
                linename = line.split("/hls/")[-1]
                #创建任务
                task = asyncio.create_task(download_ts(line,linename,session))
                tasks.append(task)
            #等待任务结束
            await asyncio.wait(tasks)

#得到密钥
def get_key(url):
    resp = requests.get(url)
    print(resp.text)
    return resp.text

async def dec_ts(name,key):
    aes = AES.new(key=key, IV=b'0000000000000000',mode=AES.MODE_CBC)
    async with aiofiles.open(f"越狱/video/{name}",mode="rb") as f1,\
        aiofiles.open(f"越狱/video2/temp_{name}",mode="wb") as f2:
        bs = await f1.read()  #从源文件读取内容
        await f2.write(aes.decrypt(bs))  #把解密好的内容写入文件
    print(f"{name}处理完毕。")

#异步解密
async def aio_dec(key):
    tasks = []
    async with aiofiles.open("越狱/越狱第一季第一集_second_m3u8.txt",mode="r",encoding="utf-8") as f:
        async for line in f:
            if line.startswith("#"):
                continue
            line = line.strip()
            linename = line.split("/hls/")[:4]
            linename_str = linename[1]
            #开始创建异步任务
            task = asyncio.create_task(dec_ts(linename_str,key))
            tasks.append(task)
        await asyncio.wait(tasks)
        

#拿到密钥
def is_key(name):
    with open(f"越狱/{name}",mode="r",encoding="utf-8") as f:
        for line in f:
            #如果以#开头则舍弃
            if line.startswith("#"):
                continue
            #去掉空格和换行符
            line = line.strip()
            line_url = line.split("/hls")[:4]
            return line_url[0]


#合并ts文件
def merge_ts():
    '''
    合并ts文件命令
    1、mac系统  cat 1.ts 2.ts 3.ts > xxx.mp4
    2、windows系统  copy /b 1.ts+2.ts+3.ts xxx.mp4
    '''
    lst = []
    with open("越狱/越狱第一季第一集_second_m3u8.txt",mode="r",encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):
                continue
            line = line.strip()
            linename = line.split("/hls/")[:4]
            linename_str = linename[1]
            lst.append(f"越狱/video2/temp_{linename_str}")
        s = "+".join(lst)
        os.system(f"copy /b {s} movie.mp4")
    print("合并完成。")

def main(url):
    #1、拿到主页面的页面源代码，m3u8的链接
    first_m3u8_url = get_iframe_src(url)
    #2、下载第一层m3u8文件
    #download_m3u8_file(first_m3u8_url,"越狱第一季第一集first_m3u8.txt")
    #3、下载第二层m3u8文件
    #读取第一层m3u8文件
    with open("越狱/越狱第一季第一集first_m3u8.txt",mode='r',encoding="utf-8") as f:
        for line in f:
            #如果以#开头则舍弃
            if line.startswith("#"):
                continue
            else:
                #去掉空白或者换行符
                line = line.strip() 
                #拼接第二层m3u8地址
                second_m3u8_url = first_m3u8_url.split("/20200901")[0] + line 
                
                #下载第二层m3u8文件
                #download_m3u8_file(second_m3u8_url,"越狱第一季第一集_second_m3u8.txt")
                print("第二层m3u8文件下载完毕。")
    
    #4、下载视频
    #异步协程
    #asyncio.run(aio_download(second_m3u8_url))
    #5、拿到密钥
    #获取密钥链接
    line_url = is_key("越狱第一季第一集_second_m3u8.txt")
    #得到密钥
    key_url = line_url + "/hls/key.key"
    key = get_key(key_url).encode("utf-8")
    #解密
    #asyncio.run(aio_dec(key))
    #6、合并ts文件为mp4文件
    merge_ts()

if __name__ == "__main__":
    url = "https://www.pianba.net/yun/25456-3-1.html"
    main(url)
