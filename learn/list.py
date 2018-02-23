l = [1, 2, 3.14, 'data'] #list
print (type(l))
l.append ([4,3])
print(l)
l.extend (['delta' ,5 ,6] )   #add  a  list
print(l)
l.insert(3, 'beta')  #insert  before  index 3
print(l)
l.remove ('data')   #delete an elementprint(l)
# 参考对象（Python features: Refer for object）
# 在Python中，如果要将值从一个对象传递给另一个对象，则=(等号)将按地址传递值。
x = [1, 2.3, 4]
y = x
y[0] = 5
print(x)
x = [1, 2, 3, 4]
z  =  x.copy()
z[0] = 5
print (x)
# 多维列表（Multidimensional  list）
a  =  [[1,2 , 3 ,4],[1,2 ,3,4],[1,2 ,3]]
print(a)
print(a[0][3])