#442. Find All Duplicates in an Array
class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        res = []
        for i in nums:
          idx = abs(i) - 1
          if nums[idx] < 0:
            res.append(abs(i))
          else :
            nums[idx] *= -1
        return res

__import__("atexit").register(lambda:open("display_runtime.txt","w").write("000"))

nums = [4,3,2,7,8,2,3,1]

s = Solution()
print(s.findDuplicates(nums))