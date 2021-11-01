from Block import Block, calculateHash
import time

class Blockchain:
    genesisBlock = Block(0, 'a8b326769ba89c5882634310a9defa17e40d0afe538a5cab7ec011e27f988281', '', 123456, 'Genesis Block')
    blockchain = [genesisBlock]

    def generateNextBlock(self, blockData):
        previousBlock = self.blockchain[-1]
        nextIndex = previousBlock.index + 1;
        nextTimestamp = time.time()
        nextHash = Block.calculateHash(nextIndex, previousBlock.hash, nextTimestamp, blockData)
        return Block(nextIndex, nextHash, previousBlock.hash, nextTimestamp, blockData)

def main():
    testBlock = Block(1, 'testBlock', 'previousTestBlock', 123, 'test')
    print(testBlock)

if __name__ == '__main__':
    main()