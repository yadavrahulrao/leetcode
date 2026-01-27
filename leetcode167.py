#219. Contains Duplicate II
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
      j= {}
      for i, n in  enumerate(nums):
          
        if n in j and i-j[n] <= k :

              return True
        j[n] = i
      return False

nums = [1,2,3,1]
k = 3
s = Solution()
print(s.containsNearbyDuplicate(nums,k))

