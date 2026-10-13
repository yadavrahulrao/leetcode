#3727. Maximum Alternating Sum of Squares

class Solution(object):
    def maxAlternatingSum(self, nums):
        list1 = [x**2 for x in nums]
        list1.sort()
        i = 0
        j = len(list1)
        mid = (i + j)//2
        a = list1[:mid]
        b = list1[mid:]
        sum_a = sum(a)
        sum_b = sum(b)
        res = sum_b - sum_a
        return res

obj = Solution()
print(obj.maxAlternatingSum([1,-1,2,-2,3,-3]))


        