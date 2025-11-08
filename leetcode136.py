class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        # Find the middle (slow will point to mid)
        prev = None
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Disconnect left half
        if prev:
            prev.next = None

        # slow is the root
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head if slow != head else None)
        root.right = self.sortedListToBST(slow.next)
        return root
