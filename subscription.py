import random
import groups
import tg
#import json

from paho.mqtt import client as mqtt_client


broker = 'inkmustang619.cloud.shiftr.io'
port = 1883
topicpython = "python/mqtt"
topicesm = "emqx/esp32"

client_id = f'subscribe-{random.randint(0, 100)}'
username = 'inkmustang619'
password = 'dnwHh6EOeyRPmJlm'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):

    def on_message(client, userdata, msg):
        isValid = False
        for i in groups.data:
            for j in i["rfidId"]:
                if j == msg: 
                    isValid = True
                    tg.tgsendmessage(groups.data.index[i])
            for j in i["fingerId"]:
                if j == msg: 
                    isValid = True
                    tg.tgsendmessage(groups.data.index[i])
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic validation is ", isValid)
        
    client.subscribe(topicpython)
    client.subscribe(topicesm)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
