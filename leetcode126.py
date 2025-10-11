#164. Maximum Gap
from math import ceil
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n<2 :
          return 0
        minv , maxv = min(nums) , max(nums)
        if minv == maxv:
          return 0

        size = ceil((maxv - minv) / (n-1))
        count = (maxv - minv) // size + 1
        b = [[float('inf'),float('-inf')] for _ in range (count)]
        for i in nums :
          idx = (i - minv) // size
          b[idx][0] = min(b[idx][0],i)
          b[idx][1] = max(b[idx][1],i)
        gap = 0
        p = minv
        for bmin , bmax in b :
          if bmin == float('inf'):
            continue
          gap = max(gap , bmin - p)
          p = bmax
        return gap

