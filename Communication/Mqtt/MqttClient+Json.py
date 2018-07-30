# coding=utf-8
import paho.mqtt.client as mqtt
import time
import json

HOST = "127.0.0.1"
PORT = 8222


# region data class


class Equipment(object):
    def __init__(self, name_in: str, id_in: int):
        self.name = name_in
        self.id = id_in


def student2dict(std):
    return {
        'name': std.name,
        'id': std.id
    }


def dict2student(d_in):
    return Equipment(d_in['name'], d_in['id'])


# endregion

# region mqtt_client


def client_loop():
    client_id = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    client_id_c_sharp = "client001"
    client = mqtt.Client(client_id_c_sharp)  # ClientId不能重复，所以使用当前时间
    client.username_pw_set("username001", password="psw001")  # 必须设置，否则会返回「Connected with result code 4」
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(HOST, PORT, 60)
    client.on_disconnect = on_disconnect  # 设置与服务器断开连接回调函数
    client.loop_forever()


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("topic/host/control")
    client_id_c_sharp = "client001"
    msg = "hello mqttSever!"
    publish(client, "slave/test", msg)


def on_message(client, userdata, msg):
    payload = msg.payload.decode("utf-8")
    print(msg.topic + " " + payload)
    if msg.topic == "topic/host/control":
        m_classS1 = Equipment(payload, 2)
        serialize_classS1 = json.dumps(m_classS1, default=student2dict)
        publish(client, "slave/json", serialize_classS1)


def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")


def publish(client, topic_in: str, msg: str):
    client.publish(topic=topic_in,
                   payload=msg,
                   qos=1,
                   retain=False
                   )


# endregion

if __name__ == '__main__':
    client_loop()
