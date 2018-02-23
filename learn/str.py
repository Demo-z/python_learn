# 字符串的str的一些功能
t='He is a string. Who are you?'
print(t.capitalize())#打印
print(t.split())#按空格将字符串转化为列表 ['He', 'is', 'a', 'string.', 'Who', 'are', 'you?']
print(t.find('i')) # return index of 'i' 返回第一个i 所在的位置
print(t.find('in')) # index of 'i' in 'in' 返回第一个in 所在的位置
print(t.find('Python')) # find sth not in  查找字符串,没有返回-1
print(t[0:4]) # returu from index 0 to 3  截取字符串  从开始到第4个
print(t.replace(' ','|')) # replace by '|'  字符串替换,空格换为 |
w = 'http://www.google.com'
print(w.strip('http://')) #delete sth 删除字符串