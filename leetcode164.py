#327. Count of Range Sum
class Solution:
    def countRangeSum(self, nums: list[int], lower: int, upper: int) -> int:
        prefix = [0]
        for x in nums :
          prefix.append(prefix[-1]+x)
        def count_sort(low,high):
          if high - low <= 1:
            return 0
          mid = (low + high)//2
          count = count_sort(low,mid) + count_sort(mid,high)
          j_low = mid 
          j_high = mid
          for i in range(low , mid):
            while j_low < high and prefix[j_low] - prefix[i] < lower :
              j_low += 1
            while j_high < high and prefix[j_high] - prefix[i] <= upper :
              j_high += 1
            count += j_high - j_low
          prefix[low:high] = sorted(prefix[low:high])
          return count
        return count_sort(0,len(prefix))
nums = [-2,5,-1]
lower = -2
upper = 2
s = Solution()
print(s.countRangeSum(nums,lower,upper))