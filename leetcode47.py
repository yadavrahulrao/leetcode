# Valid Anagram


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        # Create a frequency map for characters in s
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        # Subtract the frequencies using characters in t
        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            if count[char] < 0:
                return False
        
        return True
