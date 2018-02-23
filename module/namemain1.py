import os
def func():
    print('name.main1 中的func方法被调用')

print('name.main1 运行')
print(os.getcwd())

if __name__=='__main__':
    print('name.main1 自身运行')
else:
    print('name.main1 在其他地方调用运行')
    # 如果你在任何一个py文件中执行print(__name__), 会返回__main__，这是Python的一个内置变量，任何python文件都一样；如果你在文件A中写入print(__name__)，然后在文件B中ImportA，执行B，那么会返回A文件的文件名，而不是__main__;所以其实在代码中使用 if __name__ == '__main__', 相当于使用一个if判断，在此if条件下的内容不会在被引入模块的文件中调用，因为不是在当前py文件中直接调用，__name__会等于被引模块的文件名。
print(__name__)
