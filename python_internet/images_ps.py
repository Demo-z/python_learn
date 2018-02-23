#!usr/bin/env python
#coding:UTF-8
import urllib2
import urllib
import re
import os

# 获取页面的html
def get_page(url):
        req=urllib2.Request(url)
        try:
                html=urllib2.urlopen(req).read()
                return html
        except urllib2.URLError,e:
                if e.code==404:
                        return False

#获取美女图片的四个分类链接
def get_fen_lei_link(html):
        patt='<a href="/mm/[^\s]+?/" >'
        regex=re.compile(patt)
        fen_lei_link=[]
        temp_link=re.findall(regex,html)[0:4]
        for link in temp_link:
                fen_lei_link.append('http://www.22mm.cc'+link.split('"')[1])
        return fen_lei_link

#获取套图的链接
def get_taotu_link(specific_page):
        global taotu_links
        taotu_links={}
        patt='<a href="/[^\s]+?\.html" title=".+?"'
        regex=re.compile(patt)
        link_info=re.findall(regex,specific_page)
        for i in link_info:
                taotu_links['http://www.22mm.cc'+i.split('"')[1]]=i.split('"')[3]

#获取套图页面中指向最后一个图片的链接
def get_taotu_last_link(taotu_link):
        taotu_page=get_page(taotu_link)
        patt='<a href=\'[^\s]+?-\d+?\.html\'>\d+?</a>'
        regex=re.compile(patt)
        taotu_last_link=re.findall(regex,taotu_page)[-1].split("'")[1]
        return taotu_last_link

#获取暂时的图片链接
def get_temp_image_link(taotu_last_link):
        taotu_last_page=get_page(taotu_last_link)
        patt=patt='arrayImg\[\d\]="(http://[^\s]+?\.jpg)"'
        regex=re.compile(patt)
        temp_image_link=re.findall(regex,taotu_last_page)
        return temp_image_link

#将图片下载并且保存到D盘的pic文件夹中
def save_image(image_links,dirname):
        global index
        path=unicode('D:\\pic\\'+dirname,'utf8')
        os.mkdir('%s' %(path))
        dirname=dirname.decode('utf8')
        for img_link in image_links:
                urllib.urlretrieve(img_link,'D:\\pic\%s\%d.jpg' % (dirname,index))
                print '%s has been downloaded and saved successfully.'%(img_link)
                index+=1

def start():
        print 'Waiting............'
        url='http://www.22mm.cc'
        html=get_page(url)
        fen_lei_link=get_fen_lei_link(html)
        for link in fen_lei_link:
                temp_link=link
                page_index=1        #page_index是页面索引
                specific_page=get_page(link)
                get_taotu_link(specific_page)
                while page_index<4:        #套图的数目很多，暂时只抓取每个分类的前三页图片
                        if page_index==1:
                                specific_page=get_page(link)
                                get_taotu_link(specific_page)
                        else:
                                link=temp_link+'index_%d.html' %(page_index)
                                specific_page=get_page(link)
                                if not specific_page:
                                        break
                                else:
                                        get_taotu_link(specific_page)
                        for key in taotu_links:
                                dirname=taotu_links[key]
                                temp_taotu_last_link=get_taotu_last_link(key)
                                taotu_last_link='http://www.22mm.cc/mm/'+key.split("/")[4]+'/'+temp_taotu_last_link
                                temp_image_link=get_temp_image_link(taotu_last_link)
                                image_links=[]
                                for each in temp_image_link:
                                        image_links.append(re.sub('big','pic',each))
                                save_image(image_links,dirname)
                        page_index+=1

#links是存储套图链接信息的字典
taotu_links={}
#index是图片名称的索引
index=0
start()