import socket
import time
import threading

class p2pnetwork():

    def __init__(self, node, port):
        self.addr = ('', port)
        self.node = node
        self.peers = {}
        self.socket = None