# 89. Gray Code
class Solution:
    def grayCode(self, n: int):
        result = []
        for i in range(1 << n):   # from 0 to 2^n - 1
            result.append(i ^ (i >> 1))
        return result
