#2860. Happy Students


class Solution(object):
    def countWays(self, nums):
        
        nums.sort()
        n = len(nums)
        ans = 0

        # choose nobody
        if nums[0] > 0:
            ans += 1

        # choose everybody
        if nums[-1] < n:
            ans += 1

        # choose first k students
        for k in range(1, n):
            if nums[k - 1] < k and nums[k] > k:
                ans += 1

        return ans
        
        