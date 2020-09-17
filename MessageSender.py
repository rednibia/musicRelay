import paho.mqtt.client as mqtt
import json


class Message_Sender:

    client = mqtt.Client("mqtt_client")
    client.connect("192.168.86.177", port=1883)

    def send(self, playlist, location):
        message = dict()
        message['playlist'] = playlist
        message['location'] = location
        message_json = json.dumps(message)
        self.client.publish("music/player", message_json)
        print(message_json)
