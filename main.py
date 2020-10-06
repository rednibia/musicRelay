import json
import paho.mqtt.client as mqtt
from MusicProcessor import MusicProcessor


mqttBroker = "127.0.0.1"
mqttPort = 1883
topic = "music/playlist"

music_processor = MusicProcessor()


def on_message(client, userdata, message):
    payload = json.loads(str(message.payload.decode("utf-8")))
    print("received message: ", payload)
    music_processor.play(payload['rfid'], payload['client_id'])


def main():
    client = mqtt.Client("Music Relay")
    client.connect(mqttBroker)
    client.subscribe(topic)
    client.on_message = on_message
    client.loop_forever()


if __name__ == "__main__":
    main()
