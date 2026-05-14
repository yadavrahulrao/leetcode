#424. Longest Repeating Character Replacement
from collections import Counter
class Solution(object):
    def characterReplacement(self, s, k):
      count = Counter()
      left = 0
      j = 0
      for right , i in enumerate(s):
        count[i] += 1
        j = max(j,count[i])
        if right - left + 1 - j > k :
          count[s[left]] -= 1
          left += 1
      return len(s) - left


s = Solution()
print(s.characterReplacement("ABBBBABBBAAAAACCCCC",2))
            

        