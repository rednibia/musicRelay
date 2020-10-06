import time
import paho.mqtt.client as mqtt


mqttBroker = "127.0.0.1"
mqttPort = 1883
topic = "music/playlist"


def on_message(client, userdata, message):
    payload = str(message.payload.decode("utf-8"))
    print("received message: ", payload)


def main():
    client = mqtt.Client("Music Relay")
    client.connect(mqttBroker)
    client.subscribe(topic)
    client.on_message = on_message
    client.loop_forever()


if __name__ == "__main__":
    main()
