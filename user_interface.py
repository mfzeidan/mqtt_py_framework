import mqtt_backend as mqtt_backend

import socket
import fcntl
import struct

port = 'eth0'

server = mqtt_backend.get_ip_address(port)


topic = "mytopic"
message = "this is my first message"

#mqtt.getting_started(server,topic,message)

#mqtt.receive_messages(server, topic,message)

#mqtt.publish_messages(server,topic,message)

mqtt_backend.publish_message(server,topic,message)
