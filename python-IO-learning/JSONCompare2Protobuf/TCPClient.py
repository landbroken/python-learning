# 导入socket库:
import socket
import JSONCompare2Protobuf.GetData_JSON_Protobuf_SelfDefine as getData

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 2222))
# 接收欢迎消息:
# print(s.recv(1024).decode('utf-8'))
# 发送数据
data=getData.GetData_Protobuf()
print("data:")
print(data)
print(type(data))
s.send(data)
print("receive:data")
rec_data=s.recv(1024).decode('utf-8')
print(rec_data)
# 发送程序终止
bytes_end=b'exit'
print(bytes_end)
s.send(bytes_end)
print("receive:bytes_end")
rec_data=s.recv(1024).decode('utf-8')
print(rec_data)
# 关闭连接
s.close()