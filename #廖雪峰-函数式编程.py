# 廖雪峰-函数式编程
# 1、高阶函数Higher-order function
# 既然变量可以指向函数，函数的参数能接收变量，
# 那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
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
    x = x * x
    return x


def add3(x, y, z, f):
    return f(x) + f(y) + f(z)


ret = add3(1, 2, 3, f1)
print(ret)

# map和reduce
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce


def add(x: int, y: int):
    return x + y


ret = reduce(add, [1, 3, 5, 7, 9])
print(str(type(ret)) + ": " + str(ret))
ret = reduce(add, list(map(str, [1, 3, 5, 7, 9])))
print(str(type(ret)) + ": " + str(ret))


def fbig(x: int, y: int):
    return x * 10 + y


ret = reduce(fbig, range(1, 10, 2))
print(str(type(ret)) + ": " + str(ret))


# map/reduce练习
def normalize(name):
    return name.capitalize()  # 首字母大写，其它小写
    # .upper大写;#.lower小写;#.title所有单词首字母大写，其余小写


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# filter:根据返回值是否=true筛选元素
def is_odd(n):
    return n % 2 == 1


ret = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(ret)


# 打印1000以内的素数:
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


for n in primes():
    if n < 100:
        print(n)
    else:
        break

# filter练习-筛选回数-回数是指从左向右读和从右向左读都是一样的数
print("filter练习-筛选回数")


def is_palindrome(n):
    L1 = []
    if(n==10):
        n=n+0
    while n / 10 >= 1:
        L1.append(n % 10)  # 取最后一个数字
        n = n // 10  # 取前几位
    L1.append(n)
    lenL1 = len(L1)
    for i in range(0, lenL1 // 2 + 1):
        if (L1[i] != L1[lenL1 - i - 1]):
            return False
    return True


output = filter(is_palindrome, range(1, 1000))
print(list(output))


def retfalse(n):
    if (n % 2 == 1):
        return False
    else:
        return True


output = filter(retfalse, range(1, 6))
print(list(output))

#sorted练习
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[1]

L2 = sorted(L, key=by_name,reverse=True)
print(L2)
