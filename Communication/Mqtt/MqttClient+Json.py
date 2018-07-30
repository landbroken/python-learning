# coding=utf-8
import paho.mqtt.client as mqtt
import json

HOST = "127.0.0.1"
PORT = 8222


# region TestData class

class TestData(object):
    def __init__(self, str_in: str, str_arr_in: list, int_in: int, int_arr_in: list):
        self.str_test = str_in
        self.str_arr_test = str_arr_in
        self.int_test = int_in
        self.int_arr_test = int_arr_in


def testdata2dict(std):
    return {
        'str_test': std.str_test,
        'str_arr_test': std.str_arr_test,
        'int_test': std.int_test,
        'int_arr_test': std.int_arr_test
    }


def dict2testdata(d_in):
    return TestData(d_in['str_test'], d_in['str_arr_test'], d_in['int_test'], d_in['int_arr_test'])

# endregion

# region mqtt_client


def client_loop():
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
    client.subscribe("topic/serialize")
    msg = "hello mqttSever!"
    publish(client, "slave/test", msg)


def on_message(client, userdata, msg):
    payload = msg.payload.decode("utf-8")
    print(msg.topic + " " + payload)
    if msg.topic == "topic/host/control":
        m_class2 = TestData("str", ["str_arr1", "str_arr2"], 18, [5, 7, 9])
        serialize_class2 = json.dumps(m_class2, default=testdata2dict)
        publish(client, "slave/json", serialize_class2)
    if msg.topic == "topic/serialize":
        deserialize_class2 = json.loads(payload, object_hook=dict2testdata)
        print(deserialize_class2)


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
