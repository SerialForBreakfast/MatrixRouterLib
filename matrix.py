import socket

UDP_IP = "192.168.0.243"
UDP_PORT = "23"
MESSAGE = "IPINFO"

print "UDP Target IP:", UDP_IP
print "UDP Target PORT:", UDP_PORT
print "Message:", MESSAGE

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

sock.sendto(bytes(MESSAGE, "utf-8"),(UDP_IP, UDP_PORT))
