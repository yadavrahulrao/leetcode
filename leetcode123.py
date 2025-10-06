#169. Majority Element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        x = None
        for i in nums :
          if count == 0:
            x = i
          count += (1 if i == x else -1)
        return x
