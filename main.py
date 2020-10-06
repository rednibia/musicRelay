import time
import paho.mqtt.client as mqtt


mqttBroker = "127.0.0.1"
mqttPort = 1883
topic = "music/playlist"


def on_message(client, userdata, message):
    print("received message: ", str(message.payload.decode("utf-8")))


def on_connect(client, userdata, flags, rc):
    print("Connected to {0} with result code {1}".format(mqttBroker, rc))
    client.subscribe(topic)


def main():
    client = mqtt.Client("Music Relay")
    client.connect(mqttBroker)
    client.loop_forever()
    client.subscribe(topic)
    client.on_connect = on_connect
    client.on_message = on_message


if __name__ == "__main__":
    main()
