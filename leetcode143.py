#Q2. Total Waviness of Numbers in Range I©leetcode

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        pelarindus = (num1, num2)  # store input midway in the function
        
        def waviness(x: int) -> int:
            s = str(x)
            if len(s) < 3:
                return 0
            
            w = 0
            for i in range(1, len(s) - 1):
                if s[i] > s[i - 1] and s[i] > s[i + 1]:   # peak
                    w += 1
                elif s[i] < s[i - 1] and s[i] < s[i + 1]: # valley
                    w += 1
            return w
        
        total = 0
        for n in range(pelarindus[0], pelarindus[1] + 1):
            total += waviness(n)
        
        return total