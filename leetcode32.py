# Maximum Number of Operations to Move Ones to the End

class Solution(object):
    def maxOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        n = len(s)
        operations = 0

        while True:
            moved = False
            i = 0
            while i < n - 1:
                if s[i] == '1' and s[i + 1] == '0':
                    # Move s[i] to the right until it reaches the end or another '1'
                    j = i + 1
                    while j < n and s[j] == '0':
                        j += 1
                    # Insert the '1' just before the next '1' or at the end
                    s[i] = '0'
                    s[j - 1] = '1'
                    operations += 1
                    moved = True
                    break  # Only one operation per round
                i += 1
            if not moved:
                break
        return operations

# Example usage:
sol = Solution()
print(sol.maxOperations("1001101"))  # Output: 4
print(sol.maxOperations("00111"))    # Output: 0
