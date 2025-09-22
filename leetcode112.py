#24. Swap Nodes in Pairs
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head and head.next:
            first = head
            second = head.next

            # Swapping the pair
            prev.next = second
            first.next = second.next
            second.next = first

            # Moving to the next pair
            prev = first
            head = first.next

        return dummy.next
