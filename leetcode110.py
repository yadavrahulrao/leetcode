#28. Find the Index of the First Occurrence in a String




class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)

        # Edge case: empty needle
        if m == 0:
            return 0

        # Slide a window over haystack
        for i in range(n - m + 1):
            if haystack[i:i+m] == needle:
                return i

        return -1
