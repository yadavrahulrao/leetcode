#556. Next Greater Element III

from itertools import permutations

class Solution:
    def nextGreaterElement(self, n):
        digits = str(n)

        nums = set()

        for p in permutations(digits):
            num = int("".join(p))
            if num > n:
                nums.add(num)

        if not nums:
            return -1

        ans = min(nums)
        return ans if ans <= 2**31 - 1 else -1