#Given a non-negative integer x, 
# return the square root of x rounded down to the nearest integer.
#  The returned integer should be non-negative as well.

class Solution(object):
    def mySqrt(self,x):
        high =x
        low= 1
        while low<= high :
            mid = (low + high)//2
            mid_sqrt = mid*mid
            if mid_sqrt == x :
                return mid
            elif mid_sqrt <= x:
                low = mid +1
            else :
                high = mid -1
        return high

s = Solution()
print(s.mySqrt(4))
print(s.mySqrt(8))