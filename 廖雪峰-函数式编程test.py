#廖雪峰-函数式编程
#1、高阶函数Higher-order function
#既然变量可以指向函数，函数的参数能接收变量，
#那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
def add2(x, y, f):
    return f(x) + f(y)

'''
调用add(-5, 6, abs)相当于：
x = -5
y = 6
f = abs
f(x) + f(y) ==> abs(-5) + abs(6) ==> 11
return 11
'''
def f1(x):
    x=x*x
    return x

    
def add3(x,y,z,f):
    return f(x)+f(y)+f(z)


ret=add3(1,2,3,f1)
print(ret)

#map和reduce
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce

def add(x:int,y:int):
    return x+y


ret=reduce(add,[1, 3, 5, 7, 9])
print(ret)
ret=reduce(add,list(map(str, [1, 3, 5, 7, 9])))
print(ret)

def fbig(x:int,y:int):
    return x*10+y

ret=reduce(fbig,range(1,10,2))
print(ret)
