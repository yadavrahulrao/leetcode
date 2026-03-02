#3507. Minimum Pair Removal to Sort Array I
class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        ot = 0
        def is_sorted(arr):
            for i in range(1, len(arr)):
                if arr[i] < arr[i - 1]:
                    return False
            return True
        
        while not is_sorted(nums):
          min_sum = float('inf')
          idx = 0 
          for i in range(len(nums) - 1):
            pair_sum = nums[i] + nums[i+1]
            if pair_sum < min_sum:
              min_sum = pair_sum
              idx = i
          
          nums = nums[:idx] + [ min_sum] + nums[idx + 2 :]
          ot  += 1
        return ot 
