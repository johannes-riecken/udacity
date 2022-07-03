from typing import Callable, Optional, Set


class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next: Optional['Node'] = None

    def __repr__(self) -> str:
        return str(self.value)


class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None

    def __str__(self) -> str:
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += f"{str(cur_head.value)} -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value: int) -> None:

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self) -> int:
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1: LinkedList, llist_2: LinkedList) -> LinkedList:
    return set_operation(
            llist_1, llist_2,
            lambda v1, set_1: v1 not in set_1,
            lambda v2, set_1, set_2: v2 not in set_1 and v2 not in set_2)


def intersection(llist_1: LinkedList, llist_2: LinkedList) -> LinkedList:
    return set_operation(
            llist_1, llist_2,
            lambda v1, set_1: False,
            lambda v2, set_1, set_2: v2 in set_1 and v2 not in set_2)


def set_operation(llist_1: LinkedList, llist_2: LinkedList,
                  p_1: Callable[[int, Set[int]], bool],
                  p_2: Callable[[int, Set[int], Set[int]], bool])\
        -> LinkedList:
    ret = LinkedList()
    set_1: Set[int] = set()
    llist_1_head = llist_1.head
    while llist_1_head:
        if p_1(llist_1_head.value, set_1):
            ret.append(llist_1_head.value)
        set_1.add(llist_1_head.value)
        llist_1_head = llist_1_head.next
    llist_2_head = llist_2.head
    set_2: Set[int] = set()
    while llist_2_head:
        if p_2(llist_2_head.value, set_1, set_2):
            ret.append(llist_2_head.value)
        set_2.add(llist_2_head.value)
        llist_2_head = llist_2_head.next
    return ret


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

# 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 ->
print(union(linked_list_1, linked_list_2))
# 6 -> 4 -> 21 ->
print(intersection(linked_list_1, linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

# 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
print(union(linked_list_3, linked_list_4))
# empty string
print(intersection(linked_list_3, linked_list_4))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large
# values

# Test Case 1
print(union(LinkedList(), LinkedList()))  # empty
print(intersection(LinkedList(), LinkedList()))  # empty

# Test Case 2
linked_list_2 = LinkedList()

element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_2:
    linked_list_2.append(i)
# 6 -> 32 -> 4 -> 9 -> 1 -> 11 -> 21 ->
print(union(LinkedList(), linked_list_2))

# Test Case 3
linked_list_1 = LinkedList()

element_1 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)
# 6 -> 32 -> 4 -> 9 -> 1 -> 11 -> 21 ->
print(union(linked_list_1, LinkedList()))
