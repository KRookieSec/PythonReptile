#coding:utf-8
#抓取百度小说
# 所有章节的内容及全部章节的名称
# https://boxnovel.baidu.com/boxnovel/wiseapi/chapterList?bookid=4345130811&pageNum=1&order=asc&site=
# 章节内部的内容即章节正文
# https://h5.17k.com/ck/book/3144938/chapter/40305743?subAllPrice=1&appKey=1351550300

from asyncio import tasks
import requests
import asyncio
import aiohttp
import aiofiles
import json

'''
操作流程
1、同步操作：访问chapterList，拿到所有章节的名称和chapter_url
2、异步操作：访问chapter_url，下载所有的文章和内容
'''

async def aiodownload(cp_chapter_id, chapter_title):
    url = 'https://h5.17k.com/ck/book/3144938/chapter/'+cp_chapter_id+'?subAllPrice=1&appKey=1351550300'
    #获取章节正文
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = await resp.json()
            #使用aiofiles异步将数据保存到文件中
            async with aiofiles.open("百度小说1/"+chapter_title, mode="w",encoding="utf-8") as fp:
                await fp.write(dic['data']['content'][0]['text'])  #将小说内容写入文件  

async def GetChapterList(url):
    #发送请求
    resp = requests.get(url)
    #将页面放入字典
    dic = resp.json()
    tasks = []
    #同步操作，访问chapterList，拿到所有章节的名称和chapter_url
    for chapter_item in dic['data']['chapter']['chapterInfo']:  #chapter_item对应每个章节的名称和chapter_url
        chapter_title = chapter_item['chapter_title']   #章节名称
        chapter_url = chapter_item['chapter_url']   #章节正文链接
        cp_chapter_id = chapter_item['cp_chapter_id'] #章节正文id
        #准备异步任务
        #print(chapter_title, chapter_url)
        tasks.append(aiodownload(cp_chapter_id, chapter_title))  
    await asyncio.wait(tasks)

if __name__ == '__main__':
    url = 'https://boxnovel.baidu.com/boxnovel/wiseapi/chapterList?bookid=4345130811&pageNum=1&order=asc&site='
    asyncio.run(GetChapterList(url))