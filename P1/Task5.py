import hashlib
from typing import Optional, Dict


class Block:

    def __init__(self, timestamp: str,
                 data: str, previous_hash: Optional[str]) -> None:
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self) -> str:
        sha = hashlib.sha256()

        hash_str = self.data\
            .encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()


class Blockchain:
    def __init__(self) -> None:
        self.current_block = None
        self.blocks: Dict[str, Block] = {}

    def add_block(self, block: Block) -> None:
        self.blocks |= {block.hash: block}
        self.current_block = block

    def peek_prev(self) -> Block:
        if self.current_block is None:
            return None
        return self.blocks.get(self.current_block.previous_hash)

    def move_prev(self) -> None:
        prev = self.blocks.get(self.current_block.previous_hash)
        assert prev is not None, "no block found for previous_hash"
        self.current_block = prev


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large
# values

# Test Case 1
bc = Blockchain()
b0 = Block("11:11", "foo", None)
bc.add_block(b0)
b1 = Block("12:12", "bar", b0.hash)
bc.add_block(b1)
b2 = Block("13:13", "baz", b1.hash)
bc.add_block(b2)
print(bc.peek_prev().data)  # bar

# Test Case 2
# find first block
bc = Blockchain()
b0 = Block("11:11", "foo", None)
bc.add_block(b0)
b1 = Block("12:12", "bar", b0.hash)
bc.add_block(b1)
b2 = Block("13:13", "baz", b1.hash)
bc.add_block(b2)
b = bc.current_block
while b.previous_hash is not None:
    b = bc.blocks[b.previous_hash]
print(b.data)  # foo

# Test Case 3
# hashes are equal
b0 = Block("", "", None)
print(b0.calc_hash())
b1 = Block("12:34", "", "asdf")
print(b1.calc_hash())

# Test Case 4
bc = Blockchain()
b0 = Block("11:11", "foo", None)
bc.add_block(b0)
b1 = Block("22:22", "bar", "does_not_exist")
bc.add_block(b1)
try:
    bc.move_prev()
except Exception as e:
    print(e)  # no block found for previous_hash
