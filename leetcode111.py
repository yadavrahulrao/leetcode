#23. Merge k Sorted Lists




import heapq
from typing import List, Optional

# Definition for singly-linked list (provided by Leetcode)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Optional: For better debug printing
    def __repr__(self):
        return f"{self.val} -> {self.next}"

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Define a min-heap
        heap = []

        # Initialize heap with the head node of each list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))  # (value, list_index, node)

        # Dummy node to simplify list construction
        dummy = ListNode(0)
        current = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next

            # If the node has a next, add it to the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
