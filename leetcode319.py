#26. Remove Duplicates from Sorted Array
class Solution(object):
    def removeDuplicates(self, nums):
        list1 = []
        for i in nums:
            if i not in list1:
                list1.append(i)
        
        k = len(nums)
        nums[:k] = list1

        return k

obj = Solution()
print(obj.removeDuplicates([1,1,2]))