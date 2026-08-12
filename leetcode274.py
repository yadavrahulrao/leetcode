#Maximum Difference Between Adjacent Elements in a Circular Array
class Solution:
    def maxAdjacentDistance(self, nums):
        n = len(nums)

        res = 0
        for i in range(1, n+1):
            res = max(res, abs(nums[i-1]-nums[i % n]))
        return res