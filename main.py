import json
import paho.mqtt.client as mqtt
from MusicProcessor import MusicProcessor


mqttBroker = "127.0.0.1"
mqttPort = 1883
playlist_topic = "music/playlist"
controls_topic = "music/controls"

music_processor = MusicProcessor()


def on_message(client, userdata, message):
    if message.topic == playlist_topic:
        payload = json.loads(str(message.payload.decode("utf-8")))
        print("received playlist message: ", payload)
        music_processor.play(payload['rfid'], payload['client_id'])
    if message.topic == controls_topic:
        payload = json.loads(str(message.payload.decode("utf-8")))
        print("received playlist message: ", payload)
        # music_processor.play(payload['rfid'], payload['client_id'])


def main():
    client = mqtt.Client("Music Relay")
    client.connect(mqttBroker)
    client.subscribe(playlist_topic)
    client.subscribe(controls_topic)
    client.on_message = on_message
    client.loop_forever()


if __name__ == "__main__":
    main()
