#3863. Minimum Operations to Sort a String


class Solution(object):
    def minOperations(self, s):
        n = len(s)

        if s == ''.join(sorted(s)):
            return 0
        if n == 2 :
            return -1
        
       
        if s[0] == min(s) or s[-1] == max(s):
            return 1

        for i in range(n-1):
            if s[0] == min(s) or s[-1] == max(s):
                        return 2

        return 3
    
obj = Solution()
print(obj.minOperations("ecd"))
        