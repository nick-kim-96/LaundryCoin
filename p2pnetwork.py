import hashlib
import hmac
import socket
import time
from Message import *
import threading
import pickle

class p2pnetwork():

    def __init__(self, node, port):
        self.port = port
        self.node = node
        self.peers = {}

    def setServerSocket(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Using IPv4 protocol with TCP
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # port will be immediately reusable
        s.bind(('', port))
        s.listen(5)
        return s

    def mainLoop(self):
        s = self.setServerSocket(self.port)
        #s.settimeout(5)

        while True:
            try:
                clientSock, clientAddr = s.accept()
                clientSock.settimeout(None)

                data = clientSock.recv(1024)
                recvd_digest, pickled_data = data.split(' ')
                new_digest = hmac.new(b'shared-key', pickled_data, hashlib.sha1).hexdigest()
                if recvd_digest == new_digest:
                    new_data = pickle.loads(data)
                    self.handleData(new_data, clientSock, clientAddr)

            except KeyboardInterrupt:
                break


        s.close()


    def handleData(self, data, socket, addr):
        peer = (addr[0], data.reply_addr[1])
        data.reply_addr = peer

        if not peer in self.peers:
            threading.Thread(
                target= self.sendMessage, args= (peer, Message(Type.QUERY_LATEST_BLOCK, '', ('', self.port)))).start()



    def sendMessage(self, peer, data):
        try:
            if not peer in self.peers or True:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect(peer)
                self.peers[peer] = s
            else:
                s = self.peers[peer]
                s.connect(peer)
            s.send(pickle.dumps(data))
        except ConnectionRefusedError:
            pass