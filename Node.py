import socket
import threading
import time
import Blockchain
import p2pnetwork

class Node(threading.Thread):
    """
    An instance of a node that is able to connect to and accept connections from other nodes. Each node is part of a
    p2p network and has a copy of the blockchain.
    """
    def __init__(self, port):

        super(Node, self).__init__()

        self.port = port
        self.blockchain = Blockchain.Blockchain()
        #self.p2p = p2pnetwork.p2pnetwork(self, socket)

    def run(self):
        self.p2p.mainLoop()

    def setBlockchain(self, newChain):
        return self.blockchain.replaceChain(newChain)

    def getBlockchain(self):
        return self.blockchain.blockchain

    def addBlock(self, newBlock):
        return self.blockchain.addBlock(newBlock)
