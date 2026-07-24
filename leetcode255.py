#476. Number Complement

class Solution:
    def findComplement(self, num):
        ans = 0
        bit = 1

        while num:
            if (num & 1) == 0:
                ans |= bit
            bit <<= 1
            num >>= 1

        return ans