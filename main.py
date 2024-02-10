import random
import time
import subscription
import groups

from paho.mqtt import client as mqtt_client


broker = 'inkmustang619.cloud.shiftr.io'
port = 1883
topic = "python/mqtt"
# Generate a Client ID with the publish prefix.
client_id = f'publish-{random.randint(0, 1000)}'
username = 'inkmustang619'
password = 'dnwHh6EOeyRPmJlm'

def connect_mqtt():
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


def publish(client, recieved_msg):
    msg_count = 1
    while True:
        time.sleep(1)
        testlist = groups.rt170
        msg = msg_count
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Student num `{groups.rt170[random.randint(0, 2)]}` arrived ")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1
        if msg_count > 25:
            break


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client, 0)
    client.loop_stop()


if __name__ == '__main__':
    run()
    #subscription.run()

