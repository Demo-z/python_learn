from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page1.html")# urllib.request模块的urlopen（）获取页面  <http.client.HTTPResponse object at 0x7f8c297a4940>
bsObj = BeautifulSoup(html.read(),"html.parser")#从网页中提取的 <h1> 标签被嵌在 BeautifulSoup 对象 bsObj 结构的第二层(html → body → h1)，任 何 HTML或XML文件的任意节点信息都可以被提取出来,只要目标信息的旁边或附近有标记就行。
print(bsObj.title)
print(bsObj.html.h1)
