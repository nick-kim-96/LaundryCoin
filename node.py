import socket
import threading
import time
import Blockchain
import p2pnetwork

class Node(threading.Thread):
    """
    An instance of a node that is able to connect to and accept connections from other nodes.
    """
    def __init__(self, port):

        super(Node, self).__init__()

        self.port = port
        self.blockchain = Blockchain()
        self.p2p = p2pnetwork(self, socket)
