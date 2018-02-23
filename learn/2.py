# 1 print
# for i in range (0,5):
# 	for j in range(0,i+1):
# 		print "*",
# 	print

# 需求是这样的：传入参数 name 与 msg就可以在桌面写入文件名称和内容的函数text_create，并且如果当桌面上没有这个可以写入的文件时，
# 就要创建一个之后再写入  
# def create(name,msg): 
# 	desktop_path='/home/boom/桌面' #/home/boom/Desktop/
# 	full_path=desktop_path +name + '.txt' 
# 	file=open(full_path,'w') 
# 	file.write(msg)          
# 	file.close()
# 	print('Done') 
# create('hello','hello world')

# def text_filter(word,censored_word = 'lame',changed_word = 'Awesome'):
#     return word.replace(censored_word, changed_word)
# text_filter('Python is lame!')     # 调用函数
# middle = 5
# 1 < middle < 10

# if else
# def account_login(): 
#     password = input('Password:') 
#     if password == '12345': 
#         print('Login success!')  
#     else:   
#         print('Wrong password or invalid input!')                                             
#         account_login() 
# account_login()
# if elif else 重置密码的功能
# password_list = ['*#*#','12345']  
# def account_login():   
#     password = input('Password:')  
#     password_correct = password == password_list[-1] 
#     password_reset = password == password_list[0] 
#     if password_correct:  
#         print('Login success!') 
#     elif password_reset: 
#         new_password = input('Enter a new password:')   
#         password_list.append(new_password)  
#         print('Your password has changed successfully!') 
#         print(password_list); 
#         account_login() 
#     else: 
#         print('Wrong password or invalid input!') 
#         account_login() 
# account_login()
# loop
# for every_letter in 'Hello world':
#     print(every_letter)
# for num in range(1,11): #不包含11，因此实际范围是1～10
#     print(str(num) + ' + 1 =',num + 1)
#给登录函数增加一个新功能：输入密码错误超过3次就禁止再次输入密码
# password_list = ['*#*#','12345']

# def account_login():
#     tries = 3
#     while tries > 0:  
#         password = input('Password:')
#         password_correct = password == password_list[-1]
#         password_reset = password == password_list[0]

#         if password_correct:
#             print('Login success!')
#         elif password_reset:
#             new_password = input('Enter a new password :')
#             password_list.append(new_password)
#             print('Password has changed successfully!')
#             account_login()
#         else:
#             print('Wrong password or invalid input!')
#             tries = tries - 1  
#             print( tries, 'times left')

#     else:
#         print('Your account has been suspended')
# account_login()
# 循环方法去创建10个文本
# def create_i(num):
# 	path='/home/boom/files/'
# 	full_path=path+num+'.txt'
# 	file=open(full_path,'w')
# 	file.write(num)

# for i in range(1,11):
# 	i=str(i)//需要转换字符串类型,不然报错
# 	create_i(i)
# 教程:
# def text_creation():
# 	path='/home/boom/files'
# 	for name in range(1,11):
# 		with open(path + str(name)　+ '.txt','w') as text:
# 			text.write(atr(name))
# 			text.close()
# 			print('Done')
# text_creation()
# 复利 教程：
# def invest(amount,rate,time):
# 	print("principal amount:{}".format(amount))
# 	for t in range(1,time+1):
# 		amount=amount*(1+rate)
# 		print("year {}:${}".format(t,amount))
# money=input("you money:")
# invest(int(money),.05,8)
# invest(2000,.025,5)
# 1~100 所有的偶数   ｂｉｎｇ
# oshu=[]
# def even_print():
# 	for i in range(1,101):
# 		if i % 2 ==0:
# 			oshu.append(i)
# even_print()
# print(oshu)
a = {'key':123,'key':123}
print(a)