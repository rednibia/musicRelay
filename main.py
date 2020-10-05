from MusicController import MusicController
import paho.mqtt.client as mqtt


def on_message(client, userdata, message):
    print("received message: ", str(message.payload.decode("utf-8")))


mqttBroker = "127.0.0.1"
client = mqtt.Client("Music Relay")
client.connect(mqttBroker)

client.loop_start()

client.subscribe("music/playlist")
client.on_message = on_message
