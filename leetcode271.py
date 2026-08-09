#9. Palindrome Number

class Solution(object):
    def isPalindrome(self, x):
        if x >= 0 :
            list1 = list(str(x))
            list1.reverse()
            s = int("".join(map(str , list1)))
            if x == s :
                return True
        return False
obj = Solution()
print(obj.isPalindrome(121))
        
        