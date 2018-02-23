#coding:utf-8
from urllib.request import urlopen
# html = urlopen("http://pythonscraping.com/pages/page1.html")
#
# print(html.read())调用 html.read() 获取网页的 HTML 内容,可以把 HTML 内容传到 BeautifulSoup 对象
url = "http://www.baidu.com"
data = urlopen(url).read()
data = data.decode('UTF-8')
print(data)