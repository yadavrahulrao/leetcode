# 343. Integer Break


class Solution(object):
    def integerBreak(self, n):
        if n == 2 :
            return 1
        elif n == 3 :
            return 2
        elif n >= 4 :
            s = n // 3
            m = n % 3
            if m == 0 :
                return 3 ** s
            elif m == 2 :
                return ((3**s)*2)
            elif m == 1 :
                a = s - 1 
                return ((3**a)*4)
        
obj = Solution()
print(obj.integerBreak(19))