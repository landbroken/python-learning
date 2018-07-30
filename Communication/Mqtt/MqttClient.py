# coding=utf-8
import paho.mqtt.client as mqtt
import time

HOST = "127.0.0.1"
PORT = 8222


def client_loop():
    client_id = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    client_id_c_sharp = "client001"
    client = mqtt.Client(client_id_c_sharp)  # ClientId不能重复，所以使用当前时间
    client.username_pw_set("username001", password="psw001")  # 必须设置，否则会返回「Connected with result code 4」
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(HOST, PORT, 60)

    client.loop_forever()


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("topic/host/control")
    client_id_c_sharp = "client001"
    client.publish(topic="slave/test",
                   payload="hello mqttSever!",
                   qos=1,
                   retain=False
                   )


def on_message(client, userdata, msg):
    print(msg.topic + " " + msg.payload.decode("utf-8"))


if __name__ == '__main__':
    client_loop()
