#Union of 2 Sorted Arrays

class Solution:
    def findUnion(self, a, b):
         
        list1 = list(set(a))
        list2 = list(set(b))
        list3 = list1 + list2
        list4 = list(set(list3))
        list4.sort()
        return list4

obj = Solution()
print(obj.findUnion([1,1,1,1,1,1,1],[2,2,2,2,2,2,2]))