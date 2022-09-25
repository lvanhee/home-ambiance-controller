import socket
import pygame
import select

class from_ha_server:
  def __init__(self, PORT, processing_function):
    PORT = 65433  # Port to listen on (non-privileged ports are > 1023)
    print("Server started")

    srvsock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    srvsock.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
    srvsock.bind( ("", PORT) )
    srvsock.listen( 5 )

    descriptors = [srvsock]

    def run():

      while 1:
        #Await an event on a readable socket descriptor
        (sread, swrite, sexc) = select.select(descriptors, [], [] )
        #Iterate through the tagged read descriptors
        for sock in sread:

          #Received a connect to the server (listening) socket
          if sock == srvsock:
            accept_new_connection()
          else:

            #Received something on a client socket
            str = sock.recv(1000)

            #Check to see if the peer socket closed
            if str == '':
              host,port = sock.getpeername()
              str = 'Client left %s:%s\r\n' % (host, port)
              print( str )
              sock.close
              descriptors.remove(sock)
            else:
              host,port = sock.getpeername()
              newstr = '[%s:%s] %s' % (host, port, str)
              processing_function(str.decode("utf-8"))
              print( newstr )

    def accept_new_connection():
      newsock, (remhost, remport) = srvsock.accept()
      descriptors.append( newsock )
      str = 'Client joined %s:%s\r\n' % (remhost, remport)
      print( str )

    run()
    print("Sound server off")

    running = True
    while running:
        #for event in pygame.event.get():
        if not pygame.mixer.music.get_busy():
                print('music end event')
                running = False