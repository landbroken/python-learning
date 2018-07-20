#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

# 双向队列demo

from collections import deque

queue = deque(["Eric", "John", "Michael"])
print(queue)
queue.append("Terry")           # Terry arrives
print(queue)
queue.append("Graham")          # Graham arrives
print(queue)
left = queue.popleft()          # The first to arrive now leaves
print(left)
print(queue)
left2 = queue.popleft()         # The second to arrive now leaves
print(left2)
print(queue)                    # Remaining queue in order of arrival
queue.pop()
print(queue)                    # pop the right one
