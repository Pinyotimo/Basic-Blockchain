from blockchain import Blockchain

# Create blockchain and add blocks
my_chain = Blockchain()
my_chain.add_block("First block data")
my_chain.add_block("Second block data")

# Display the blockchain
for block in my_chain.chain:
    print(f"Block {block.index}:\nHash: {block.hash}\nData: {block.data}\n")