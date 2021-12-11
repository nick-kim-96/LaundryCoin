import socket
import Node
import p2pnetwork
import threading

class Server:

    def __init__(self, node, port):
        self.port = port
        self.socket = None
        self.node = node

    def run(self, _):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Using IPv4 protocol with TCP
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # port will be immediately reusable
        self.socket.bind(('', self.port))
        self.socket.listen(1)

        while True:
            try:
                clientSock, clientAddr = self.socket.accept()
                clientSock.settimeout(None)
                data = clientSock.recv(1024)

                path = data.split()[1]

                if path == b'/' or path == b'/blocks':
                    clientSock.send(b'HTTP/1.0 200 OK \r\n\r\n')
                    for block in self.node.getBlockchain():
                        clientSock.send(str(block).encode())
                elif path == b'/mine':
                    clientSock.send(b'HTTP1.0 200 OK \r\n\r\n')
                    new_block = self.node.createBlock('hi')
                    clientSock.send(str(new_block).encode())

                clientSock.close()
            except IOError:
                break

        socket.close()

def main():
    node = Node.Node(1)
    server = Server(node, 2)
    threading.Thread(target=server.run, args=(None,)).start()
    #node.run()
    print('Node running on port {}'.format(2))




if __name__ == '__main__':
    main()