#coding:utf-8
#xpath解析
from lxml import etree

xml = """
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id="10086">周大强</nick>
        <nick id="10010">周芷若</nick>
        <nick class="joy">周杰伦</nick>
        <nick class="jolin">蔡依林</nick>
        <div>
            <nick>惹了</nick>
        </div>
        <span>
            <nick>热</nick>
        </span>
    </author>

    <partner>
        <nick id="ppc">胖胖陈</nick>
        <nick id="ppbc">胖胖不陈</nick>
    </partner>
</book>
"""
tree = etree.XML(xml)
#result = tree.xpath("/book")     #/表示层级关系，第一个/是根节点
#result = tree.xpath("/book/name")
#result = tree.xpath("/book/name/text()")   #text()拿文本,name标签下的文本
#result = tree.xpath("/book/author/nick/text()")   #text()拿/author/nick/标签下的文本
#result = tree.xpath("/book/author//nick/text()")  #text()拿author节点下的所有nick文本
#result = tree.xpath("/book/author/*/nick/text()")  #text()拿author节点下任意标签的nick文本
result = tree.xpath("/book//nick/text()")  #text()拿author节点下的所有nick文本
print(result)