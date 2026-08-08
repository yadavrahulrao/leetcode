# 7 . reverse integer 

class Solution(object):
    def reverse(self, x):
        sign = 1
        if x < 0 :
            sign = -1
        x = abs(x)
        
        splt = [int(i) for i in str(x)]
        splt.reverse()
        res = int("".join(map(str,splt)))
        if x < 0 and res > -2**31 and res < 2**31 -1:

            return sign*res
        elif res > -2**31 and res < 2**31 -1:
            return sign*res
        else :
            return 0
        
obj = Solution()
print(obj.reverse(123))
