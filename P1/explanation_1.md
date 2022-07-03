Task 1 (LRU Cache)
==================

- `get` time complexity is independent of elements processed, O(1)
- `set` time complexity is independent of elements processed, O(1)
- The cache size is also asymptotically independent of the items added, as it
  can't grow over capacity.


Task 2 (find files)
===================

- O(n) for both time and space, where n is the number of entries (and is the
  number of matching files in the worst case)

Task 3 (Huffman coding)
=======================

- O(n) for time where n is len(data)
- O(n) for space, too, in the worst case (no compression achievable)

Task 4 (Active directory)
=========================

- Time complexity in worst case: O(n^m) where n is the average number of users
  in a group and m the average nesting of groups
- Space complexity: O(n) where n is the total number of users

Task 5 (Blockchain)
===================

- As it's a linked list, it has the same time and space complexity as a linked
  list (time O(1) for insertion or deletion at one place, O(n) for navigating to an element, space O(n))

Task 6 (Linked list intersection and union)
===========================================

As I've implemented both union and intersection using the same skeleton, they
have the same space and time complexity.
- Space in worst case is O(n + m), where n and m are the two lists' lengths.
- Time complexity in worst case is also O(n + m)
