#Write a function to find the longest common prefix string amongst an array of strings.

class Solution:
    def longestCommonPrefix(self, strs):
        # Edge case: if the list is empty, return an empty string
        if not strs:
            return ""
        
        # Start by assuming the first string is the longest common prefix
        prefix = strs[0]
        
        for string in strs[1:]:
            # Compare the prefix with each string
            while not string.startswith(prefix):
                # Shorten the prefix by one character
                prefix = prefix[:-1]
                # If there is no common prefix, return an empty string
                if not prefix:
                    return ""
        
        return prefix
