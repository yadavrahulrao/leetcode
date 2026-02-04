# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []

        # Push digits into stacks
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next

        carry = 0
        head = None

        # Pop from stacks and build result
        while s1 or s2 or carry:
            x = s1.pop() if s1 else 0
            y = s2.pop() if s2 else 0

            total = x + y + carry
            carry = total // 10

            node = ListNode(total % 10)
            node.next = head
            head = node

        return head


# Helper function: build linked list from Python list
def build_linked_list(nums):
    head = None
    for num in reversed(nums):
        head = ListNode(num, head)
    return head


# Helper function: print linked list
def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# ---- TEST CASE ----
if __name__ == "__main__":
    # Input: 7243 + 564
    l1 = build_linked_list([7, 2, 4, 3])
    l2 = build_linked_list([5, 6, 4])

    print("List 1:")
    print_linked_list(l1)

    print("List 2:")
    print_linked_list(l2)

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    print("Result:")
    print_linked_list(result)
