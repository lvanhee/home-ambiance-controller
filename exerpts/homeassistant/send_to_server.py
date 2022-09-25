import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

# Connect to the server

clientSocket.connect(("192.168.0.141", 65432));

# Send data to server

data = "tyrill_yes";

clientSocket.send(data.encode());

# Receive data from server

dataFromServer = clientSocket.recv(1024);

# Print to the console

print(dataFromServer.decode());