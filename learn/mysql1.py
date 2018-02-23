import pymysql
#建立数据库连接
conn= pymysql.connect(
    host='localhost',
    user='root',
    passwd='1234',
    db='demo',
    port=3306)
cur = conn.cursor()
sql = "insert into demo1 (id,content,time) values ('', '你好', 124)"

try:
    cur.execute(sql) #执行sql语句
    conn.commit()
    print ('insert OK!!', cursor.rowcount, ' rows')
except:
    conn.rollback()
    print('Alert')
cur.close()
conn.close
