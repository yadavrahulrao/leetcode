#707. Design Linked List

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1

        curr = self.head

        for _ in range(index):
            curr = curr.next

        return curr.val

    def addAtHead(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def addAtTail(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
        else:
            curr = self.head

            while curr.next:
                curr = curr.next

            curr.next = new_node

        self.size += 1

    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
            return

        if index == self.size:
            self.addAtTail(val)
            return

        curr = self.head

        # Stop at the node just before index
        for _ in range(index - 1):
            curr = curr.next

        new_node = Node(val)
        new_node.next = curr.next
        curr.next = new_node

        self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return

        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return

        curr = self.head

        # Stop at the node just before index
        for _ in range(index - 1):
            curr = curr.next

        curr.next = curr.next.next
        self.size -= 1
