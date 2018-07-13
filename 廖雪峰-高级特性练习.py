#廖雪峰-高级特性-列表生成式练习
# -*- coding: utf-8 -*-
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print(L2)

#生成器-generator
def FibonacciGenerator(max):
    ai=0
    aj=1
    n=1
    while n<max:
        print(aj)
        ai,aj=aj,ai+aj
        n=n+1
    return 'done'

#如果一个函数定义中包含yield关键字，
#那么这个函数就不再是一个普通函数，而是一个generator：
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f=fib(6)

g = fib(6)
while True:
     try:
         x = next(g)
         print('g:', x)
     except StopIteration as e:
         print('Generator return value:', e.value)
         break


#生成器练习
#杨辉三角
import copy

def triangles():
    n=0
    Now=[]
    Last=[]
    while True:
        n=n+1
        Now.append(1)
        for x in range(1,n-1):
            Now[x]=Last[x-1]+Last[x]
        Last=copy.deepcopy(Now)    
        yield Now

        
def trianglesFor(max):
    n=0
    Now=[]
    Last=[]
    while n<max:
        n=n+1
        Now.append(1)
        for x in range(1,n-1):
            Now[x]=Last[x-1]+Last[x]
        Last=copy.deepcopy(Now)
        print(Now)
        
            
trianglesFor(5)

# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
