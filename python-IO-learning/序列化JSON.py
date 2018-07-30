import json
from collections import OrderedDict

class Student(object):
    def __init__(self, name_in: str, age_in: int):
        self.name = name_in
        self.age = age_in


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age
    }


def dict2student(d_in):
    return Student(d_in['name'], d_in['age'])


# 序列化变量
# d = dict(name='Bob', age=20, score=88)
#d = OrderedDict(UserCreate=0, U="admin", P="admin",newUsers=[],newPwd=[])
newUsers=[]
newPwd=[]
newLevel=[]
newUsers.append("ostartj")
newUsers.append("ostartj2")
newPwd.append("ostar123")
newPwd.append("ostar123")
newLevel.append(1)
newLevel.append(1)
d=[]
d.append("Cmd=UserCreate")
d.append("U=admin")
d.append("P=admin")
d.append("U="+str(newUsers))
d.append("P="+str(newPwd))
d.append("Level="+str(newLevel))
serialize_dictV = json.dumps(d)
print("d:")
print(d)
print(type(d))
#print(len
print("serialize_dictV:")
print(serialize_dictV)
print(type(serialize_dictV))
#print("len(serialize_dictV):")
print(len(serialize_dictV))

d2=bytes("{UserCreate&U=admin&P=admin&U=ostartj,U=ostartj2&P=ostar123,P=ostar123&Level=1,Level=1}".encode())
print(d2)
print(len(d2))
d3=bytes(serialize_dictV.encode())
print(d3)
print(len(d3))

# 序列化类
m_classS1 = Student("mike", 18)
print("新建m_classS1类并输出：")
print(m_classS1)
serialize_classS1 = json.dumps(m_classS1,default=student2dict)
# serialize_classS1 = json.dumps(m_classS1, default=lambda obj: obj.__dict__)
print("序列化m_classS1类并输出：")
print(serialize_classS1)
print(type(serialize_classS1))
print(len(serialize_classS1))
# 反序列化类
deserialize_classS1 = json.loads(serialize_classS1, object_hook=dict2student)
print(deserialize_classS1)
print(type(deserialize_classS1))
