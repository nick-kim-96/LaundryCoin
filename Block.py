import hashlib

class Block:
    def __init__(self, index, hash, previousHash, timestamp, data):
        """
        Block Constructor
        :param index: (int)
        :param hash: (String)
        :param previousHash: (String)
        :param timestamp: (int)
        :param data: (String)
        """
        self.index = index
        self.hash = hash
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.data = data

    """
    def calculateHash(self):
        return calculateHash(self.index, self.previousHash, self.timestamp, self.data)
    """

