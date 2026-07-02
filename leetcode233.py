#2094. Finding 3-Digit Even Numbers

from itertools import permutations

class Solution(object):
    def findEvenNumbers(self, digits):
        s = list(set(digits))
        c = list(set(permutations(digits,3)))
        res = [int("".join(map(str,i))) for i in c if i[0] != 0]
        
        return s 
        
        ans = []
        
        for i in res:
            if i % 2 == 0 :
                ans.append(i)
        
        return sorted(ans)
    
    
obj = Solution()
print(obj.findEvenNumbers([1,3,7,0,3,5,4,7,8,6,0,9,5,3]))