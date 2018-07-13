import threading
import asyncio
import time
"""
hello()会首先打印出Hello world!，
然后，yield from语法可以让我们方便地调用另一个generator。
由于asyncio.sleep()也是一个coroutine，
所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环。
当asyncio.sleep()返回时，线程就可以从yield from拿到返回值（此处是None），
然后接着执行下一行语句。

把asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，
而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行。
"""
@asyncio.coroutine
def hello():
    startTime=time.time()
    print("Hello world!"+str(startTime))
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(2)
    endTime=time.time()
    print("Hello again!"+str(endTime))
    print("Time span is: "+str(endTime-startTime))

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()

