import socket

#clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
#clientSocket.connect(("192.168.0.141", 65432));

clientSocket_main_ha = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
clientSocket_main_ha.connect(("homeassistant", 65433));

#def send(msg):
 #   clientSocket.send(msg.encode())

def send_to_main_ha(msg):
    clientSocket_main_ha.send(msg.encode())
