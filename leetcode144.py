#Q1. Minimum Number of Flips to Reverse Binary String©leetcode

class Solution:
    def minimumFlips(self, n: int) -> int:
        s = bin(n)[2:]      # Convert to binary string without leading zeros
        r = s[::-1]         # Reverse the string
        
        flips = 0
        for i in range(len(s)):
            if s[i] != r[i]:
                flips += 1
        
        return flips