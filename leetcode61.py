#382. Linked List Random Node



class Solution:

    def __init__(self, head: Optional[ListNode]):
      self.arr = []
      current = head
      while current is not None:
         self.arr.append(current.val)
         current= current.next
        

    def getRandom(self) -> int:
       return self.arr[random.randrange(len(self.arr))]
     