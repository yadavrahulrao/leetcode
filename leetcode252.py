#561. Array Partition

class Solution(object):
    def arrayPairSum(self, nums):
        s = sorted(nums)
        pair = list(zip(s[::2],s[1::2]))
        mins = [min(i) for i in pair]
        return sum(mins)
    
obj = Solution()
print(obj.arrayPairSum([6,2,6,5,1,2]))
        