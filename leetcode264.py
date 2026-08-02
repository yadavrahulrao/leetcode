class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            s = target - nums[i]
            if s in nums[i+1:]:
                return [i,nums.index(s,i+1)]
                
            
obj = Solution()
print(obj.twoSum([3,3],6))
        