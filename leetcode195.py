#409. Longest Palindrome
class Solution:
    def longestPalindrome(self, s: str) -> int:
        # odd = sum(v %2 for v in Counter(s).values())
        # return len(s) - odd + (1 if odd else 0)

        count = Counter(s)
        leng = 0
        odd = False
        for i in count.values():
            if i % 2 == 0:
                leng += i 
            else :
                leng += i -1 
                odd = True
        if odd :
            leng += 1
        return leng