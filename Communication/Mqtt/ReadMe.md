# 参考文献
[1]Python paho-mqtt 模块使用和API分析
https://blog.csdn.net/youshenmebutuo/article/details/79779387#12publish

[2]Python MQTT客户端实现
https://blog.csdn.net/itas109/article/details/78873257

# MqttClient.py
是client示例，示例实现功能包括：
* 1、client连接客户端；
* 2、连接时触发事件；
* 3、订阅消息；
* 4、接收订阅消息时触发事件；
* 5、发布消息

# MqttPublish.py
是单次publish示例
> import paho.mqtt.publish as publish

# MqttClient+Json
是演示了用mqtt发送序列化json

publish.single自动连接mqtt服务器，
发布一次消息，然后自动断开