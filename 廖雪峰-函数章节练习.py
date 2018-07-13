import math

'''廖雪峰，python，函数章节练习'''
def my_abs(x:int):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

para1=12
para2=6
sum=my_abs(para1)
print(sum)

x, y = move(100, 100, 60, math.pi / 6)
r=move(100, 100, 60, math.pi / 6)#返回多值其实就是返回一个tuple
print(x, y)
print(r)

def quadratic(a,b,c):
    delta=b**2-4*a*c
    ret=0;
    if(delta<0):
        raise ValueError('no real root')
    elif(delta==0):
        ret=-b/(2*a)
        return (ret,ret)
    else:
        ret1=(-b+math.sqrt(delta))/(2*a)
        ret2=(-b-math.sqrt(delta))/(2*a)
        return (ret1,ret2)

print(quadratic(2, 3, 1)) # => (-0.5, -1.0)
print(quadratic(1, 3, -4)) # => (1.0, -4.0)

#默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

#默认参数必须指向不变对象！
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

a=power(5)
b=power(5, 3)
print(a,b)
c=add_end()
d=add_end()
e=add_end([1,2,2,3])
print(c,d,e)

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

a=calc(1, 2)
b=calc(1, 3, 5, 7)
nums = [1, 2, 3]
c=calc(*nums)
print(a,b,c)

#关键字参数
'''
#关键字参数允许你传入0个或任意个含参数名的参数
#这些关键字参数在函数内部自动组装为一个dict
'''

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
