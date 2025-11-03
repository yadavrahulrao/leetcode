# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_head = ListNode(0)
        after_head = ListNode(0)

        before = before_head
        after = after_head

        # Traverse the linked list
        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next

        # Connect the two partitions
        after.next = None  # Important to terminate the list
        before.next = after_head.next

        # The head of the new list is before_head.next
        return before_head.next
