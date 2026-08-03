#217. Contains Duplicate

class Solution(object):
    def containsDuplicate(self, nums):
        
        n = len(nums)
        
        s = list(set(nums))
        
        d = len(s)
        
        if n != d :
            return True
        return False
    
obj = Solution()
print(obj.containsDuplicate([1,2,3,1]))
        
        
        