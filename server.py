import socket
import threading

class sever:

    def __init__(self, port):
        self.port = port
        self.socket = None
