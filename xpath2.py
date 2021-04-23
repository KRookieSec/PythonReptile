#coding:utf-8
from lxml import etree

tree = etree.parse("b.html")   #使用etree()读取文件
#result = tree.xpath('/html')
#result = tree.xpath("/html/body/ul/li/a/text()")   #读取a标签下的文本
#result = tree.xpath("/html/body/ul/li[1]/a/text()") #读取第一个li标签下的a标签文本，xpath的顺序从1开始，[]表示索引
#result = tree.xpath("/html/body/ol/li/a[@href='dapao']/text()")   #@表示属性
#print(result)
ol_li_list = tree.xpath("/html/body/ol/li")
for li in ol_li_list:
    #print(li)
    #从每一个li中提取到文字信息
    result = li.xpath("./a/text()")   #在li中继续寻找a标签文本
    print(result)
    result2 = li.xpath("./a/@href")   #拿到属性值：@属性
    print(result2)
print(tree.xpath("/html/body/ul/li/a/@href"))  #拿到ul标签下所有a标签的href属性值
