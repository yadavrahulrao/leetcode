#1652. Defuse the Bomb


class Solution(object):
    def decrypt(self, code, k):
        n = len(code)
        if k == 0 :
            return [0] * n
        
        res = []
        for i in range(n):
            p = 0
            if k > 0 :
                for j in range(1,k+1):
                    p += code[(i+j)%n]
                    
            else :
                for j in range(1,-k+1):
                    p += code[(i-j)%n]
            
            res.append(p)
            
        return res
    
obj = Solution()
print(obj.decrypt([2,4,9,3],-2))


n = int(input("enter n :"))
s = n % 4
print(s)

            
        