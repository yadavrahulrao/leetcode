#430. Flatten a Multilevel Doubly Linked List




class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        p = head

        while p:
          if p.child:
            nxt = p.next
            child = p.child
            p.next = child
            child.prev = p
            p.child  = None
            while child.next :
              child = child.next
            child.next = nxt 
            if nxt:
              nxt.prev = child
                 
          p = p.next
        return head