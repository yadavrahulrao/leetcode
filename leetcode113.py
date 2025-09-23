#25. Reverse Nodes in k-Group
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Step 1: Check if there are at least k nodes to reverse
        count = 0
        node = head
        while node and count < k:
            node = node.next
            count += 1
        if count < k:
            return head  # Not enough nodes to reverse, return head as is

        # Step 2: Reverse k nodes
        prev = None
        curr = head
        next_node = None
        for _ in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Step 3: head is now the tail of the reversed group, connect with next part
        head.next = self.reverseKGroup(curr, k)

        # Step 4: prev is the new head of the reversed group
        return prev
