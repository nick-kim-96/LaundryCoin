class Block:

    def __init__(self, index, hash, previousHash, timestamp, data):
        self.index = index
        self.hash = hash
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.data = data