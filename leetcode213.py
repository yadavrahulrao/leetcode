#977. Squares of a Sorted Array
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        """
        sq = [x**2 for x in nums]
        sq.sort()
        return sq
        # lst = []
        # for i in nums:
        #   lst.append(abs(i))
          
        # lst.sort()
        # squ = [x**2 for x in lst]
        # return squ
s = Solution()
print(s.sortedSquares([-4,-1,0,3,10]))