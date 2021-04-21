#coding:utf-8
#抓取优美图库的图片
#一、拿到主页面的源代码，然后提取到子页面的链接地址，href
#二、通过href拿到子页面的内容，从子页面中找到图片的下载地址 img->src
#三、下载图片
import requests
from bs4 import BeautifulSoup
import time
import warnings
warnings.filterwarnings("ignore")
#1、配置url
url = "https://www.youmeitu.com/weimeitupian"
headers = {
    "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
}
resp = requests.get(url)
resp.encoding = 'utf-8'
#print(resp.text)
#把源代码交给bs
main_page = BeautifulSoup(resp.text,"html.parser")
#拿到class="TypeList"下所有的a标签
alist = main_page.find("div",class_="TypeList").find_all("a",class_="TypeBigPics")
#print(alist)
for a in alist:
    child_url = a.get('href')   #通过get就可以拿到属性值
    #print(child_url)
    #拿到子页面的源代码
    href = url+child_url
    #print(href)
    child_page_resp = requests.get(href)
    child_page_resp.encoding = 'utf-8'
    chile_page_text = child_page_resp.text
    #从子页面中拿到图片的下载路径
    child_page = BeautifulSoup(chile_page_text,"html.parser")
    #通过特殊标记定位到图片的下载地址处
    p = child_page.find("p",align="center")
    #定位到img标签
    img = p.find("img")
    #print(img)
    src = "https://www.youmeitu.com"+img.get("src")
    #print(src)
    #下载图片
    img_resp = requests.get(src)
    #img_resp.content   #这里拿到的是字节
    img_name = src.split("/")[-1]   #拿到url中最后一个/后的内容
    with open("img/"+img_name,mode="wb") as f:
        f.write(img_resp.content)   #图片内容写入文件
    print("Over!",img_name)
    time.sleep(1)     #休息1秒再继续，防止被服务器封禁
resp.close()
print("Reptile over!")
