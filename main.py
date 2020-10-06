import time
import paho.mqtt.client as mqtt


mqttBroker = "127.0.0.1"
mqttPort = 1883
topic = "music/playlist"


def on_message(client, userdata, message):
    print("received message: ", str(message.payload.decode("utf-8")))


def main():
    client = mqtt.Client("Music Relay")
    client.connect(mqttBroker)
    client.loop_forever()
    client.subscribe(topic)
    client.on_message = on_message


if __name__ == "__main__":
    main()
