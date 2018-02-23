#!/usr/bin/env python
# coding:UTF-8
import urllib
import re
import os
import os.path

index = 0


# 抓取页面的函数
def getPage(url):
    page = urllib.urlopen(url).read()
    return page


# 抓取首页美女分类的链接信息
def getSortLinkInfo(html):
    patt = '<a href="/[^\s]+?\.html" title="[^\s]+?"'
    regex = re.compile(patt)
    linkInfo = re.findall(regex, html)
    links = {}
    for i in linkInfo:
        # links.append('http://www.22mm.cc'+i.split('"')[1])
        links['http://www.22mm.cc' + i.split('"')[1]] = i.split('"')[3]
    return links  # links是有效链接的列表


# 获取特定美女页面中的链接信息
def getBeautyLinkInfo(link):
    page = getPage(link)
    patt = '<a href=\'[^\s]+?-\d+?\.html\'>\d+?</a>'
    regex = re.compile(patt)
    lastLink = re.findall(regex, page)
    if len(lastLink) > 0:
        lastLink = lastLink[-1].split("'")[1]
    return lastLink  # lastLink是最后一个美女页面的相对路径


# 提取最终美女图片的链接
def getImgLinks(lastLink):
    page = getPage(lastLink)
    patt = 'arrayImg\[0\]="(http://[^\s]+?\.jpg)"'
    regex = re.compile(patt)
    imgLinks = re.findall(regex, page)
    return imgLinks  # imgLinks是有效的图片链接的列表


# 下载并且保存图片
def saveImg(imgLinks, dirname):
    global index
    path = unicode('D:\\pics\\' + dirname, 'utf8')
    os.mkdir('%s' % (path))
    dirname = dirname.decode('utf8')
    for i in imgLinks:
        urllib.urlretrieve(i, 'D:\\pics\%s\%d.jpg' % (dirname, index))
        print
        '%s has been downloaded and saved successfully.' % (i)
        index += 1


indexURL = 'http://www.22mm.cc'


def start():
    homePage = getPage(indexURL)
    links = getSortLinkInfo(homePage)
    for i in links:
        # dirname=unicode('D:\\pics\\'+links[i],'utf8')
        # os.mkdir('%s' %(dirname))
        dirname = links[i]
        relPath = getBeautyLinkInfo(i)
        if len(relPath) > 0:
            lastLink = 'http://www.22mm.cc/mm/' + i.split("/")[4] + '/' + relPath
            tempLinks = getImgLinks(lastLink)
            imgLinks = []
            for j in tempLinks:
                imgLinks.append(re.sub('big', 'pic', j))
            saveImg(imgLinks, dirname)


start()