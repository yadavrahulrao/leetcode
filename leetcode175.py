#215. Kth Largest Element in an Array

import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        return heapq.nlargest(k,nums)[-1]


nums = [3,2,1,5,6,4]
k = 2

s = Solution()
print(s.findKthLargest(nums,k))