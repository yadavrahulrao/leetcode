#268. Missing Number
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)

        t_sum = n*(n+1)//2

        a_sum = sum(nums)

        missing = t_sum - a_sum 
        return missing 