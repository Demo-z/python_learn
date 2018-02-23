import os
# http://blog.csdn.net/liang19890820/article/details/78218051
# import commands

print(os.name)# os.name字符串指示你正在使用的平台。可获取当前的操作系统所代表的字符串  Linux/Unix 为‘posix‘ ，windows 为’nt‘
print(os.getcwd())# 获取当前的工作目录，即python脚本工作的目录路径

# print(os.getenv("SystemRoot"))
# 由结果可知，函数os.getenv(varname)对于参数中的varname是不区分大小写的。当varname不存在时，函数会返回None作为结果返回。
# print(os.putenv(varname,value))# 设置环境变量
# print(os.unsetenv(varname))# 删除一个环境变量
print(os.listdir('/var/www'))# 以列表的形式返回指定目录下的所有文件和目录名
# print(os.remove('/var/www/pycharm/ceshi.py'))# 用来删除指定文件 返回None
# Python执行系统命令的方法 os.system()，os.popen()，commands
# http://blog.51cto.com/codemaid/1899698
# print(os.system('cat /var/www/pycharm/module/os.py'))# 无法获得到输出和返回值的
#
# output = os.popen('cat /var/www/pycharm/module/os.py')
# print(output.read())
# (status, output) = commands.getstatusoutput('cat /var/www/pycharm/module/os.py')
# print(status, output)
print(os.linesep) # 字符串给出当前平台使用的行终止符。例如，Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'。在linux 系统中可呈现换行的效果
print(os.path.split('/var/www/pycharm/module/os.py'))# 返回一个路径的目录名和文件名
print(os.path.isfile('/var/www/pycharm/module/os.py'))# True 检验给出的路径是一个文件还是目录(文件)
print(os.path.isdir('/var/www/pycharm/module/os.py'))# False 检验给出的路径是一个文件还是目录(目录)
print(os.path.exists('/var/www/pycharm/module/os.py'))# True 验给出的路径是否真的存在
print(os.path.exists('/media/boom/闲适/ceshi/'))
# remove(path) 删除文件
# rmdir(path)　删除目录，只能删除空目录
# import shutil
# >>> shutil.rmtree("Py")  # 删除非空目录
# print(__name__)