#350. Intersection of Two Arrays II


# from typing import List --- this will convert list -> List.
from collections import Counter
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) > len(nums2):
          nums1,nums2 = nums2,nums1
        counts = Counter(nums1)
        res = []
        for n in nums2:
          if counts[n] > 0:
            res.append(n)
            counts[n] -= 1
        return res
nums1 = [1,2,2,1]
nums2 = [2,2]
s = Solution()
print(s.intersect(nums1,nums2))