#389. Find the Difference
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = 0 
        for c in s :
          d ^= ord(c)
        
        for c in t :
          d ^= ord(c)
        
        return chr(d)