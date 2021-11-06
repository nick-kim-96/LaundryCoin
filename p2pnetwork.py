import socket
import time
import threading

class p2pnetwork():

    def __init__(self, node, port):
        self.port = port
        self.node = node
        self.peers = {}

    def setServerSocket(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Using IPv4 protocol with TCP
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # port will be immediately reusable
        s.bind(('', port))
        socket.listen(5)
        return s

    def mainLoop(self):
        socket = self.setServerSocket(self.port)
        socket.settimeout(2)

        while True:
            try:
                clientSock, clientAddr = socket.accept()


            except KeyboardInterrupt:
                break

            except:
                continue
