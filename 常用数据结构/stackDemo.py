#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

# 直接用list当成栈来用
stack = [-1]
print(stack)
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
stack.pop(-1)  # 或者stack.pop()是一样的
print(stack)
top = stack[-1]
print(top)
