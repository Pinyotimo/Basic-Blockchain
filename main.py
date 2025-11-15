import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", time.time(), "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), latest_block.hash, time.time(), data)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.calculate_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
        return True

# Example usage
my_blockchain = Blockchain()
my_blockchain.add_block("First block data")
my_blockchain.add_block("Second block data")

for block in my_blockchain.chain:
    print(f"Block {block.index}:\nHash: {block.hash}\nData: {block.data}\n")