import hashlib

class BCoinBlock:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = ' - '.join(transaction_list) + ' - ' + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

# BC - BCoin
t1 = 'Bright sends 4.09 BC to Bobby'
t2 = 'Nzube sends 3 BC to Gift'
t3 = 'Blessing sends 6.9 BC to Ebuka'
t4 = 'Ify sends 2.5 BC to Onyedikachi'
t5 = 'Onyebuchi sends 1.2 BC to Sunday'
t6 = 'Bright sends 100 BC to Sarah'

initial_block = BCoinBlock('First Block', [t1, t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = BCoinBlock(initial_block.block_hash, [t3, t4])

print(second_block.block_data)
print(second_block.block_hash)

third_block = BCoinBlock(second_block.block_hash, [t5, t6])

print(third_block.block_data)
print(third_block.block_hash)
