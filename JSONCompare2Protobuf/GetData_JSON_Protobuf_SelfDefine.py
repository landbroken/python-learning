import json
import protobufTest.testCreate_pb2 as userCreate

"""
JSON数据构造
"""
def GetData_JSON():
    newUsers = []
    newPwd = []
    newLevel = []
    newUsers.append("ostartj")
    newUsers.append("ostartj2")
    newPwd.append("ostar123")
    newPwd.append("ostar123")
    newLevel.append(1)
    newLevel.append(1)
    data_JSON = []
    data_JSON.append("Cmd=UserCreate")
    data_JSON.append("U=admin")
    data_JSON.append("P=admin")
    data_JSON.append("U=" + str(newUsers))
    data_JSON.append("P=" + str(newPwd))
    data_JSON.append("Level=" + str(newLevel))
    serialize_dictV = json.dumps(data_JSON)
    return serialize_dictV

def GetData_Protobuf():
    admin = userCreate.Admin()
    admin.Cmd = "UserCreate"
    admin.U = "admin"
    admin.P = "admin"
    NewUser1 = admin.newUs.add()
    NewUser1.N = "ostartj"
    NewUser1.P = "ostar123"
    NewUser1.Level = 1
    NewUser2 = admin.newUs.add()
    NewUser2.N = "ostartj2"
    NewUser2.P = "ostar123"
    NewUser2.Level = 1
    ret=admin.SerializeToString()
    return ret

def GetData_SelfDefine():
    data = bytes("{UserCreate&U=admin&P=admin&U=ostartj,U=ostartj2&P=ostar123,P=ostar123&Level=1,Level=1}".encode())
    return data