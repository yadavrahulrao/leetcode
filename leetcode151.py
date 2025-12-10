#387. First Unique Character in a String
class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        freq = Counter(s)  # Count occurrences of each character
        
        for i, ch in enumerate(s):
            if freq[ch] == 1:
                return i
        
        return -1
