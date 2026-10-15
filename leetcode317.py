class Solution(object):
    def sumCounts(self, nums):
        n = len(nums)
        arr = []
        for i in range(n):
            for j in range(i,n):
                arr.append(len(set(nums[i:j+1])))
        res = [x**2 for x in arr]
        return sum(res)

obj = Solution()
print(obj.sumCounts([1,2,1]))
        