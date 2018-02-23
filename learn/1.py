# age=12
# if age>18:
#     print("wedf as")
# else:
#     print("sdf")
# print('\u4e2d\u6587')  中文
# print(chr(66))  B
# -*- coding: utf-8 -*-
# print(len('中国文'))   3
# print(len('中国文'.encode('utf-8')))   9 .decode('utf-8')
# print('Hi, %s, you have $%d.' % ('Michael', 1000000))  Hi, Michael, you have $1000000.
# %运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略
# print('pjsbh %s' % 'dnk')
# print('pjsbh %d' % 'dnk')
# print('pjsbh %d' % 2343)
# print('pjsbh %d kj %s' %(2342,234))
# print('hello ,{0},sdg,{1:.1f}%'.format('速度快放假吧',23.234))  hello ,速度快放假吧,sdg,23.2%

#list
# classmates = ['Michael', 'Bob', 'Tracy']   列表  列
# print(classmates[-1],classmates[1])   Tracy Bob
# classmates.append('Google') 在 刚才的列中添加新元素
# del classmates[1]  删除元素
# classmates.insert(1, 'Jack')  元素插入到指定的位置，比如索引号为1的位置：
# classmates.pop() 删除list末尾的元素，用pop()方法
# classmates.pop(1) 删除指定位置的元素，用pop(i)方法，其中i是索引位置
# classmates[1] = 'Sarah' 某个元素替换成别的元素，可以直接赋值给对应的索引位置
# s = ['python', 'java', ['asp', 'php'], 'scheme']  list元素也可以是另一个list
# print(classmates)

# tuple
# classmates = ('Michael', 'Bob', 'Tracy')
# classmates[0]
# print(classmates[0])
# age=-1
# if age>1:
# 	print('小明的年龄：'+str(age))    #print('小明的年龄：',str(age))
# elif age<-3:  #上一步执行成功，这里就不走了
# 	print("wef")
# else:
# 	print("kbsf")

# for
# classmates = ['Michael', 'Bob', 'Tracy']
# for mate in classmates: #一定要记得加冒号
# 	print(mate)
# sum =0
# for x in [1,2,3,4,5,6,7]:
# 	print(x)
# 	sum=sum+x
# print(sum);   #28
# a=list(range(8))
# print(a)
# for x in a:
# 	print(x)
# 	sum=sum+x
# print(sum)
 
# # while 
# sum = 0
# n = 99
# while n > 0:
#     sum = sum + n
#     n = n - 2
# print(sum)

# # while + break
# n = 1
# while n <= 100:
#     if n > 10: # 当n = 11时，条件满足，执行break语句
#         break # break语句会结束当前循环
#     print(n)
#     n = n + 1
# print('END')

# while + continue
# n = 0
# while n < 10:
#     n = n + 1
#     if n % 2 == 0: # 如果n是偶数，执行continue语句
#         continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
# print(n)
# d={'2':3,'3':3,'4':4}
# d['23'] = 43
# # print('23' in d) True
# # print('2233' in d) False
# print(d['23'])  43
# print(d['2']); 3

# dict
# d={'2':3,3:34,'4':4}
# print(d.get('2'))  3  键为 '2'
# print(d.get(2)) None  没有键为 2   返回None的时候Python的交互环境不显示结果
# print(d.get(3)) 34   键为 3 
# print(d.get(34,-1))   -1  如果没有 键 就输出默认值  删除一个key，用pop(key)方法，对应的value也会从dict中删除
# d.pop(3)  删除一个key，用pop(key)方法，对应的value也会从dict中删除
# print(d)  {'2': 3, '4': 4}

# set
# s=set([1,2,3])  {1, 2, 3}
# s=set([1,1,2,2,3,3]) {1, 2, 3}
# s=set([1,2,3]) 
# s.add(4)   添加
# s.remove(3) 删除
# s1=set([1,2,3])
# s2=set([2,3,4])
# print(s1&s2)   取交集
# print(s1|s2)   取并集


# 函数
# print(help(abs))
# print(abs(-123))  求绝对值的函数abs
# print(max(1,3,4)) 求最大值 返回最大的
# print(int('23'))  
# print(int(23.1))   23
# print(str(2342.3))  2342.3
# print(float('23'))  23.0
# print(bool('23'))  True
# print(bool(''))   False
# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
# a=abs   变量a指向abs函数
# print(a(-1))  所以也可以通过a调用abs函数

# 定义一个函数 def   用print  直接写函数名就行，不用再次打印  用return 需要 print  打印   
# 用from abstest import my_abs来导入my_abs()函数，注意abstest是文件名（不含.py扩展名）
# 可以返回多个值  逗号隔开
# def myfunction (x):
# 	if x>0:
# 		# print(x)
# 		return x
# 	elif x<-3:
# 		# print("-3")
# 		return -3
# 	else:
# 		# print("-2")
# 		return -2
# print(myfunction(-1))

# def my_abs(x):
#     if not isinstance(x, (int, float)):    isinstance() 函数  自动检测数据类型
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x
# 空函数   pass   如果想定义一个什么事也不做的空函数，可以用pass语句
# def nop():
#     pass
# import math  载入 math  包  可引用 包内函数

# def power(x):
# 	return x*x
# print(power(3));
# 函数参数问题
# def power(x,n):
# 	s=1
# 	while n>0:
# 		n=n-1
# 		s=s*x
# 	return s
# print(power(3,3))


# 定义默认参数要牢记一点：默认参数必须指向不变对象！
# def list(l=[]):
# 	l.append('end')
# 	return l
# print(list(l=['1','2']))  ['1', '2', 'end']
# print(list())  ['end']
# print(list())  ['end', 'end']
# 修改后
# def list(l=None):   str None  是不变对象
#     if l is None:
#         l = []
#     l.append('END')
#     return l
# print(list())   ['END']
# print(list())   ['END']
