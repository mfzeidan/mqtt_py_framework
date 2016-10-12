import mqtt_framework as mqtt

import socket
import fcntl
import struct

port = 'eth0'

server = mqtt.get_ip_address(port)


topic = "mytopic"
message = "this is my first message"

#mqtt.getting_started(server,topic,message)

#mqtt.receive_messages(server, topic,message)

#mqtt.publish_messages(server,topic,message)

damsg = mqtt.test()

damsg.publish_msg()
