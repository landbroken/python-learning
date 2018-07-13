'''
#可以添加自己的搜索目录
>>> import sys
>>> sys.path.append('/Users/michael/my_py_scripts')
'''
#作用域
def __get1():
    return 5

def _get2():
    return 7

def add(a,b):
    return a+b

def add():
    return __get1()+_get2()

if __name__=='__main__':
    a=add()
    print(r"add(): " + str(a))
