#Reverse Linked List



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        current = head

        while current:
            next_node = current.next  # store the next node
            current.next = prev       # reverse the link
            prev = current            # move prev and current one step forward
            current = next_node

        return prev  # prev is the new head

