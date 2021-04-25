#coding:utf-8
#防盗链处理，爬取梨视频
'''
一、拿到contId
二、拿到videoStatus返回的json. -> srcURL
三、srcURL里面的内容进行修整
四、下载视频
'''
import requests
#主页面url
url = "https://www.pearvideo.com/video_1727779"
#获取contId
contId = url.split("_")[1]
#获取视频链接，contId为视频下载地址参数，mrd为随机数
videoStatusURL = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.6990362282015661"
#伪造UA
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/535.36",
    #防盗链,请求下一个页面时对本级页面的上一级的链接进行溯源，溯源不到时返回错误无法访问下一级链接
    "Referer": url
}
#发起请求
resp = requests.get(videoStatusURL,headers=headers)
#获取响应数据
dic = resp.json()
#配置响应参数
srcUrl = dic['videoInfo']['videos']['srcUrl']
systemTime = dic['systemTime']
#配置视频真正的下载链接srcUrl
srcUrl = srcUrl.replace(systemTime, f"cont-{contId}")
#print(srcUrl)
#下载视频
with open("a1.mp4",mode="wb") as f:
    f.write(requests.get(srcUrl).content)
    f.close()
print("Reptile over!")