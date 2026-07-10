#90. Subsets II



class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        n = len(nums)

        res = set()

        for mask in range(1 << n):
            subset = []

            for i in range(n):
                if mask & (1 << i):
                    subset.append(nums[i])

            res.add(tuple(subset))

        return [list(x) for x in res]