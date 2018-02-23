# 创建一个文件 (Creating new file)
file = open('newfile.txt', 'w')
file.write('I am created for the course. \n')
file.write('How about you? ')
file.write('How is your exam?')
file.close()

# 读取一个文件 (Reading a file)
file = open('newfile.txt', 'r')
#show whole efile
print(file.read())
#show first ten characterrs
print(file.read(10))
#view by line
print(file.readline())
#view all by line
print(file.readlines())
file.close()

# 循环读取一个文件 (Looping over a file object)
file = open('newfile.txt', 'r')
for  line  in  file:
     print (line)
file.close()

# 增加一个文件 (Adding in a file)

file = open（'newfile.txt', 'a')
file.write('\nI am back again. \n'）
file.write('Do  you miss me?\n')
file.clase()

# with语句  (The with statement)
# 很容易忘记关闭{close()}文件。 由于这个和其他原因，最好使用with语句:
# 这样可以确保文件正确关闭，即使读取时发生错误
with open(“humpty.txt”) as f：

# 文件路径  (File paths)
# 也可以使用绝对路径指定文件名。
# 反斜杠需要转义（写入两次'\'）
open('/etc/gimp/2.O/gtkrc')