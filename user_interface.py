import mqtt_framework as mqtt

server = "192.168.0.1"
topic = "mytopic"
message = "this is my first message"

mqtt.getting_started(server,topic,message)
