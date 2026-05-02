#81. Search in Rotated Sorted Array II
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        if target in nums:
          return True
        else :
          return False

s = Solution()
d = s.search([2,5,6,0,0,1,2],4)
print(d)