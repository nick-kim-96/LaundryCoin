import hashlib

class Block:
    def __init__(self, index, hash, previousHash, timestamp, data):
        """
        Block Constructor
        :param index: (int)
        :param hash: (String)
        :param previousHash: (String)
        :param timestamp: (float)
        :param data: (String)
        """
        self.index = index
        self.hash = hash
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.data = data

    def __str__(self):
        return 'Block {}:\n-data: {}\n-timestamp: {}\n-hash: {}\n-prev_hash: {}\n'.format(
            self.index,
            self.data,
            self.timestamp,
            self.hash,
            self.previousHash
        )