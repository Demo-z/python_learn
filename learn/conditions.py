# 条件语句 (Example & exercise: conditions)
# 对于多条件同时使用的情况，我么使用and, or 或者 not作为关键字来相互衔接
a = [24, 16, 54]
b = []
if  a[0]< a[1]  and a[0]< a[2] :
    b.append(a[0])
    if  a[1]  <  a[2]:
        b.append(a[1])
        b.append(a[2])
    else:
        b.append(a[2])
        b.append(a[1])