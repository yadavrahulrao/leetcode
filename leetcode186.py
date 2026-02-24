#494. Target Sum
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        if abs(target) > total or (target + total) % 2 != 0 :
          return 0
        subset_sum = (target + total) // 2
    
        dp = [0] * (subset_sum + 1)
        dp[0] = 1  # One way to make sum 0 (choose nothing)
    
        for num in nums:
          for s in range(subset_sum, num - 1, -1):
            dp[s] += dp[s - num]
    
        return dp[subset_sum]