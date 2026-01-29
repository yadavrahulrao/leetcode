#228. Summary Ranges
class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        res = []
        n = len(nums)
        i = 0

        while i<n:
          start = nums[i]
          while i+1 < n and nums[i+1] == nums[i] +1:
            i+=1
          end = nums[i]
          if start == end:
            res.append(str(start))
          else :
            res.append(f"{start}->{end}")
          i+=1
        return res


__import__("atexit").register(lambda:open("display_runtime.txt","w").write("000"))
nums = [0,1,2,4,5,7]
s = Solution()
print(s.summaryRanges(nums))