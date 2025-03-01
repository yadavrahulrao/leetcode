#Roman to Integer


class Solution:
    def __init__(self):
        self.roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def romanToInt(self, s):  
        total = 0
        for i in range(len(s) - 1):
            if self.roman_map[s[i]] < self.roman_map[s[i + 1]]:
                total -= self.roman_map[s[i]]
            else:
                total += self.roman_map[s[i]]
        total += self.roman_map[s[-1]]
        return total
param_1 = "MCMXCIV"
ret = Solution().romanToInt(param_1)
print(ret)  
