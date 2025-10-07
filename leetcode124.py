#47. Permutations II
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        path = []

        use = [False] * len(nums)

        def back():
          if len(path) == len(nums):
            res.append(list(path))
            return
          
          for i in range(len(nums)):

            if use[i]:
              continue

            if i > 0 and nums[i] == nums[i-1] and not use[i-1]:
              continue

            use[i] = True
            path.append(nums[i])
            back()
            path.pop()
            use[i] = False
        back()
        return res

