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

    def calculateHash(self):
        return calculateHash(self.index, self.previousHash, self.timestamp, self.data)

def calculateHash(index, previousHash, timestamp, data):
    """
    Note: A block can’t be modified without changing the hash of every consecutive block.
    :param index: (int) the index of a block.
    :param previousHash: (String) the hash of the previous block.
    :param timestamp: (int) the timestamp of a block.
    :param data: (String) the data of a block.
    :return: (String) crpytographic hash of a block.
    """
    return hashlib.sha256((str(index) + previousHash + str(timestamp) + data).encode('utf-8')).hexdigest()


def main():
    testBlock = Block(1, 'testBlock', 'previousTestBlock', 123, 'test')
    print(testBlock.calculateHash())

if __name__ == '__main__':
    main()