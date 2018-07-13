#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pickle

class Student(object):
    def __init__(self,nameIn,ageIn):
        self.name=nameIn
        self.age=ageIn

d = dict(name='Bob', age=20, score=88)
serialize_d = pickle.dumps(d)
print(type(serialize_d))
print(serialize_d)

m_strV="1234"
m_intV=1234
m_byteV="1234".encode()
print(type(m_byteV))
print(len(m_byteV))
print(m_byteV)
serialize_strV=pickle.dumps(m_strV)
serialize_intV=pickle.dumps(m_intV)
serialize_byteV=pickle.dumps(m_byteV)
print(serialize_strV)
print(serialize_intV)
print(serialize_byteV)
print(len(serialize_strV))
print(len(serialize_intV))
print(len(serialize_byteV))

m_classS1=Student("mike",18)
print(m_classS1)
serialize_classS1=pickle.dumps(m_classS1)
print(serialize_classS1)
print(len(serialize_classS1))
