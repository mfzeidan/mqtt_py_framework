import socket
import fcntl
import struct	

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])


def getting_started(server,topic,message):
    print "You're now connected to " + str(server)
    print "You're now publishing your messages to " + str(topic)
    print "You just sent " + str(message) + " to the following topic " + str(topic)

def receive_messages(device_ip,topic,message):
   print "You are now subscribed to device " + str(device_ip) + " on the topic: " + str(topic)


def publish_messages(device_ip,topic_to_publish_to,message_to_publish):
   print "you've just published message: " + str(message_to_publish) + " to " + str(device_ip)

class test:
   def publish_msg():
      print "hi"


   

