# 347. Top K Frequent Elements
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        for num in nums:
          count[num] = count.get(num, 0) + 1

        sorted_items = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))
        return list(sorted_items)[:k]

s = Solution()
print(s.topKFrequent([4,1,-1,2,-1,2,3], 2))
      