#3639. Minimum Time to Activate String
from typing import List

class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        n = len(s)

        # Helper function to count valid substrings after placing '*' at positions in 'starred'
        def count_valid_substrings(starred: List[bool]) -> int:
            invalid = 0
            i = 0
            while i < n:
                if starred[i]:
                    i += 1
                    continue
                j = i
                while j < n and not starred[j]:
                    j += 1
                length = j - i
                invalid += (length * (length + 1)) // 2
                i = j
            total = (n * (n + 1)) // 2
            return total - invalid

        # Binary search for minimum t
        left, right = 0, n - 1
        ans = -1

        while left <= right:
            mid = (left + right) // 2
            # Apply '*' to first (mid + 1) positions in order
            starred = [False] * n
            for i in range(mid + 1):
                starred[order[i]] = True

            valid = count_valid_substrings(starred)

            if valid >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
