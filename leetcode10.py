#You are given a large integer represented as an integer array digits,
#  where each digits[i] is the ith digit of the integer.
#  The digits are ordered from most significant to least significant in left-to-right order. 
# The large integer does not contain any leading 0's.

class Solution:


    def plusOne(self, digits):
        
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
solution = Solution()
print(solution.plusOne([1, 2, 3]))  
print(solution.plusOne([4, 3, 2, 1]))  
print(solution.plusOne([9])) 
