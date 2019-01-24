#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 内置异常类继承关系见https://docs.python.org/3/library/exceptions.html#exception-hierarchy
import logging
import time

Logger = logging.getLogger("tryLearning")
file_handler = logging.FileHandler("test.log")
Logger.addHandler(file_handler)
# 格式化输出
dateNow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
service_name = dateNow + "  tryLearning"
Logger.error('%s service is down!', service_name)


def foo(a: int, b: int):
    try:
        ret = a / b
    except ZeroDivisionError as e:
        print("except:", e)
        Logger.exception(e)
        ret = -1
    except Exception as e:
        print('Error:', e)
        logging.exception(e)
        ret = -2
    finally:
        print("finally")
    print("End")
    return ret


'''
except: division by zero
return -1
'''
print(foo(1, 0))
