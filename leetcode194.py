#linear search 

# list = [1,3,4,5,6,87,9]

# n = int(input("enter the number:"))


# if n in list:
#   print("found")
# else :
#   print("not found")


# def linear(arr,target):
#   for i in range(len(arr)):
#     if arr[i] == target:
#       return i
#   return -1

# arr = [1,2,3,4,5,6,7,8,9]
# target = int(input("enter the value:"))

# s = linear(arr,target)

# if s != -1:
#   print("found")
# else :
#   print("not found")



#82. Remove Duplicates from Sorted List II
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        loc = ListNode(0)
        loc.next = head
        prev = loc

        while head:
          if head.next and head.val == head.next.val:
            while head.next and head.val == head.next.val:
              head = head.next
            prev.next = head.next
          
          else :
            prev = prev.next
          
          head = head.next
        return loc.next