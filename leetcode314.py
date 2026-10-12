#2778. Sum of Squares of Special Elements 

class Solution(object):
    def sumOfSquares(self, nums):
        n = len(nums)
        # list1 = []
        # for i in range(0,n):
        #     if n % (i+1) == 0 :
        #         list1.append(nums[i])
        # list2 = [x**2 for x in list1]
        # sums = sum(list2)
        # return sums
        total  = 0
        for i  in range(0,n):
            if n % (i+1) == 0:
                total += nums[i] ** 2
        return total
obj = Solution()
print(obj.sumOfSquares([2,7,1,19,18,3]))
        