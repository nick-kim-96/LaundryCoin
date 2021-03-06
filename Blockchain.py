from Block import *
import time
import hashlib

class Blockchain:

    def __init__(self):
        self.genesisBlock = Block(0, 'a8b326769ba89c5882634310a9defa17e40d0afe538a5cab7ec011e27f988281', '', 123456, 'Genesis Block')
        self.blockchain = [self.genesisBlock]

    def calculateHash(self, index, previousHash, timestamp, data):
        """
        Note: A block can’t be modified without changing the hash of every consecutive block.
        :param index: (int) the index of a block.
        :param previousHash: (String) the hash of the previous block.
        :param timestamp: (int) the timestamp of a block.
        :param data: (String) the data of a block.
        :return: (String) crpytographic hash of a block.
        """
        return hashlib.sha256((str(index) + previousHash + str(timestamp) + data).encode('utf-8')).hexdigest()

    def calculateHashForBlock(self, block):
        return self.calculateHash(block.index, block.previousHash, block.timestamp, block.data)

    def generateNextBlock(self, blockData):
        previousBlock = self.blockchain[-1]
        nextIndex = previousBlock.index + 1;
        nextTimestamp = time.time()  #float
        nextHash = self.calculateHash(nextIndex, previousBlock.hash, nextTimestamp, blockData)
        return Block(nextIndex, nextHash, previousBlock.hash, nextTimestamp, blockData)

    def isValidNewBlock(self, newBlock, previousBlock):
        if not self.isValidBlockStructure(newBlock):
            print('invalid structure')
            return False

        if previousBlock.index + 1 != newBlock.index:
            print('invalid index')
            return False
        elif previousBlock.hash != newBlock.previousHash:
            print('invalid previoushash')
            return False
        elif self.calculateHashForBlock(newBlock) != newBlock.hash:
            print('invalid hash')
            return False
        return True

    def isValidBlockStructure(self, block):
        """
        Note: When comparing types, it is better to use == instead of keyword 'is'.
        :param block: The block to validate.
        :return: Whether the structure of the block is valid.
        """
        return type(block.index) == int \
               and type(block.hash) == str \
               and type(block.previousHash) == str \
               and type(block.timestamp) == float \
               and type(block.data) == str

    def isValidChain(self, chain):
        def isValidGenesis(block):
            return block is self.genesisBlock

        if not isValidGenesis(chain[0]):
            return False

        for i in range(1, len(chain)):
            if not self.isValidNewBlock(chain[i], chain[i - 1]):
                return False
        return True

    def addBlock(self, newBlock):
        if self.isValidNewBlock(newBlock, self.blockchain[-1]):
            self.blockchain.append(newBlock)
            return True
        return False

    def replaceChain(self, newChain):
        if self.isValidChain(newChain) and len(newChain) > len(self.blockchain):
            print('Received blockchain is valid. Replacing current blockchain with received blockchain.')
            self.blockchain = newChain
            return True
        else:
            print('Received blockchain is invalid.')
            return False

