#!/usr/bin/python3
# coding = utf-8

from xml.dom.minidom import parse
import xml.dom.minidom

# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse("movies.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
    msg = "Root element : %s" % collection.getAttribute("shelf")
    print(msg)

# 在集合中获取所有电影
movies = collection.getElementsByTagName("movie")

# 打印每部电影的详细信息
for movie in movies:
    print
    "*****Movie*****"
    if movie.hasAttribute("title"):
        msg = "Title: %s" % movie.getAttribute("title")
        print(msg)

    tagType = movie.getElementsByTagName('type')[0]
    msg = "Type: %s" % tagType.childNodes[0].data
    print(msg)
    tagFormat = movie.getElementsByTagName('format')[0]
    msg = "Format: %s" % tagFormat.childNodes[0].data
    print(msg)
    rating = movie.getElementsByTagName('rating')[0]
    msg = "Rating: %s" % rating.childNodes[0].data
    print(msg)
    description = movie.getElementsByTagName('description')[0]
    msg = "Description: %s" % description.childNodes[0].data
    print(msg)

