import socket
import Node
import p2pnetwork
import threading

class Server:

    def __init__(self,node, port):
        self.port = port
        self.socket = None
        self.node = node

    def run(self, _):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Using IPv4 protocol with TCP
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # port will be immediately reusable
        s.bind(('', self.port))
        s.listen(1)

        while True:
            try:
                clientSock, clientAddr = s.accept()
                clientSock.settimeout(None)
                data = clientSock.recv(1024)

                path = clientSock.split()[1]

                if path == b'/':
                    clientSock.send(b'HTTP/1.0 200 OK \r\n\r\n')
            except IOError:
                break

        s.close()

def main():
    node = Node.Node(1)
    server = Server(node, 1)
    threading.Thread(target=server.run, args=(None,)).start()
    print('Node running on port {}'.format(1))




if __name__ == '__main__':
    main()