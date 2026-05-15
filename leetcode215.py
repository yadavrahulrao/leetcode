#875. Koko Eating Bananas
class Solution(object):
    def minEatingSpeed(self, piles, h):
      
      low = 1
      high = max(piles)
      while low < high :
        mid = low + (high-low) // 2
        count = 0
        for i in piles:
          count += (i + mid  - 1) // mid

        if count <=  h :
            high = mid
        else :
            low = mid + 1
      return low

s = Solution()
print(s.minEatingSpeed([3,6,7,11],8))
        