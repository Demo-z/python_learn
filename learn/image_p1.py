#!/usr/bin/python3.5
# import re
# import urllib

# def getHtml(url):
#     page = urllib.request.urlopen(url)
#     html = page.read()
#     return html

# print(getHtml("https://ip.nowtool.cn/iptance/"))
import MySQLdb
conn= MySQLdb.connect(
    host='localhost',
    user='root',
    passwd='1234',
    db='demo',
    port=3306)
cur = conn.cursor()
sql = "insert into demo1 (id,content,time) values (, '12', 124)"

try:
    cur.execute(sql) 
    conn.commit()
    print ('insert OK!!', cursor.rowcount, ' rows')
except:
    conn.rollback()
    print('Alert')
cur.close()
conn.close
