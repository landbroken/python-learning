import threading
import asyncio
import time
import random


def ioTime(ran: float):
    if ran >= 0.8:
        return 10
    elif ran>=0.5:
        return 5
    elif ran>=0.3:
        return 1
    else:
        return 0.1


@asyncio.coroutine
def hello():
    ran = random.random()  # 0.2的概率IO堵塞很久
    curIOTime = ioTime(ran)
    startTime = time.time()
    print('Hello world! (%s)' % threading.currentThread())
    print("now: "+str(startTime)+"  ioTime = "+str(curIOTime))
    yield from asyncio.sleep(curIOTime)
    endTime = time.time()
    print('Hello again! (%s)' % threading.currentThread())
    print(str(endTime))
    print("Time span is: " + str(endTime) + " - " + str(startTime) + " = " + str(endTime - startTime))


loop = asyncio.get_event_loop()
tasks = [hello(), hello(), hello(), hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
