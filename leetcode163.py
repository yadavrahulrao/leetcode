# x = 4
# y = 1
# z = (x+y)//2
# print(z)

#367. Valid Perfect Square
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 1 
        high = num
        while low <= high :
          mid = (low + high )//2
          sqrt = mid * mid
          if sqrt == num :
            return True
          elif sqrt <= num :
            low = mid + 1
          else :
            high = mid -1
        return False
s = Solution()
print(s.isPerfectSquare(9))
print(s.isPerfectSquare(8))