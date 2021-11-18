import socket
import Node
import threading

class Server:

    def __init__(self,node, port):
        self.port = port
        self.socket = None
        self.node = node

    def run(self, _):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Using IPv4 protocol with TCP
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # port will be immediately reusable
        self.socket.bind(('', self.port))
        self.socket.listen(1)

        while True:
            conn_socket, addr = self.socket.accept()
            try:
                message = conn_socket.recv(1024)
                endpoint = message.split()[1]
                if endpoint == b'/' or endpoint == b'/blocks':
                    conn_socket.send(b'HTTP/1.0 200 OK\r\n\r\n')
                    for block in self.node.getBlockchain():
                        conn_socket.send(str(block).encode())

                conn_socket.close()
            except IOError:
                conn_socket.close()
        control_socket.close()

def main():
    node = Node.Node(1)
    server = Server(node, 2)
    threading.Thread(target=server.run, args=(None,)).start()
    print('Node running on port {}'.format(2))




if __name__ == '__main__':
    main()