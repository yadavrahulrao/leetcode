#268. Missing Number

class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        for i in range(n+1):
            if i not in nums:
                return i
obj = Solution()
print(obj.missingNumber([3,0,1]))
            

            
        