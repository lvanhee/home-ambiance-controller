import socket
import socketserver

HOST = "0.0.0.0"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

class hwRequestHandler( socketserver.StreamRequestHandler ):
  def handle( self ):
   print("Hello World!\n")


server = socketserver.TCPServer( ("", PORT), hwRequestHandler )
server.serve_forever()



##
print("Server started")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            else:
                print(data)
            #conn.sendall(data)
