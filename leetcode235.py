#198. House Robber
class Solution(object):
    def rob(self, nums):
        a = 0
        b = 0
        for i in nums:
            c = max(a,b+i)
            b = a
            a = c
        return a

obj = Solution()
print(obj.rob([100,10,1,10,100]))