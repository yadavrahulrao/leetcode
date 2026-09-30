#Palindrome String

class Solution:
    def isPalindrome(self, s):
        # code here
        x = 0 
        y = len(s)-1
        
        def rever(s, x , y ):

            if x >= y :
                return True
            
            if s[x] != s[y] :
                return False
            return rever(s,x+1,y-1)
        return rever(s,x,y)
        
obj = Solution()
print(obj.isPalindrome("abba"))

        
