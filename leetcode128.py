#414. Third Maximum Number
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1,n):
          temp = nums[i]
          j = i-1
          while j>=0 and nums[j] > temp:
            nums[j+1] = nums[j]
            j -= 1
          nums[j+1] = temp

        l = []
        for k in nums:
          if k not in l:
            l.append(k)
        
        if len(l) >= 3:
          return l[-3]
        else :
          return l[-1]


