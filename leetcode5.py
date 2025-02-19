#Given an integer array nums, 
# return true if any value appears at least twice in the array, 
# and return false if every element is distinct.



class Solution(object):
    def containsDuplicate(self, nums):
        x = set()
        for i in nums:
            if i in x :
                return True
            x.add(i)      
        return False
s = Solution()
nums = [1,2,3,1]
s.containsDuplicate(nums)
