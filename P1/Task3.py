import sys
from collections import Counter
from queue import PriorityQueue
from dataclasses import dataclass
from typing import Optional, Tuple, Dict
from functools import total_ordering, reduce


@dataclass
@total_ordering
class Freq:
    freq: int
    obj: Optional[str]

    def __eq__(self, other: object) -> bool:
        return self.freq == other.freq if isinstance(other, Freq) else NotImplemented

    def __lt__(self, other: object) -> bool:
        return self.freq < other.freq if isinstance(other, Freq) else NotImplemented


@dataclass
@total_ordering
class Tree:
    val: Freq
    left: Optional['Tree']
    right: Optional['Tree']

    def __eq__(self, other: object) -> bool:
        return self.val == other.val if isinstance(other, Tree) else NotImplemented

    def __lt__(self, other: object) -> bool:
        return self.val < other.val if isinstance(other, Tree) else NotImplemented


def huffman_encoding(data: str) -> Tuple[str, Tree]:
    frequencies: Counter[str] = Counter()
    # I leave this case out, so that I have a stronger return type
    assert data != ""
    for d in data:
        frequencies[d] += 1
    q: PriorityQueue[Tree] = PriorityQueue()
    for k, v in dict(frequencies).items():
        q.put(Tree(Freq(v, k), None, None))
    while q.qsize() > 1:
        x = q.get_nowait()
        y = q.get_nowait()
        inner = Freq(x.val.freq + y.val.freq, None)
        t = Tree(inner, x, y)
        q.put(t)
    t = q.get_nowait()
    codes = get_codes(t)
    encoded = reduce(lambda a, b: a + b, [codes[x] for x in data])
    return encoded, t


def get_codes(t: Tree, path: str = "", m: Dict[str, str] = {}) -> Dict[str, str]:
    if t.left is None or t.right is None:
        assert t.val.obj is not None, 'invariant "obj set at leaves" not held'
        return m | {t.val.obj: path}
    return get_codes(t.left, f"{path}0", m) | get_codes(t.right, f"{path}1", m)


def huffman_decoding(data: str, tree: Tree) -> str:
    codes = {v: k for k, v in get_codes(tree).items()}
    buf = ""
    decoded = ""
    for x in data:
        buf += x
        char = codes.get(buf)
        if char is not None:
            decoded += char
            buf = ""
    assert len(buf) == 0, "couldn't recognize all codes"
    return decoded


if __name__ == "__main__":
    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n"  # 69
          .format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, a_great_tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n"  # 36
          .format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, a_great_tree)

    print("The size of the decoded data is: {}\n"  # 69
          .format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large
# values

# Test Case 1
a_great_sentence = "AAAAAAABBBCCCCCCCDDEEEEEE"

print("The size of the data is: {}\n"  # 74
      .format(sys.getsizeof(a_great_sentence)))
print("The content of the data is: {}\n".format(a_great_sentence))

encoded_data, a_great_tree = huffman_encoding(a_great_sentence)

# equals 1010101010101000100100111111111111111000000010101010101
print(encoded_data)
# equals a_great_sentence
print(huffman_decoding(encoded_data, a_great_tree))


# Test Case 2
a_great_sentence = ""
try:
    encoded_data, a_great_tree = huffman_encoding(a_great_sentence)
except Exception as e:
    print(e)  # wont' encode empty data

decoded_data = huffman_decoding("", Tree(Freq(1, 'asdf'), None, None))
print(decoded_data)  # empty string

# Test Case 3
try:
    decoded_data = huffman_decoding("abc", Tree(Freq(1, 'asdf'), None, None))
except Exception as e:
    print(e)  # couldn't recognize all codes
