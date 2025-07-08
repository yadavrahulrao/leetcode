# 151. Reverse Words in a String
# Medium
# Topics
# premium lock iconCompanies

# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be
#  separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces 
# between two words. The returned string should only have a single space separating the words.
#  Do not include any extra spaces.

 

# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"

# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.

# Example 3:

# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space 
# in the reversed string.

 

# Constraints:

#     1 <= s.length <= 104
#     s contains English letters (upper-case and lower-case), digits, and spaces ' '.
#     There is at least one word in s.



class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Step 1: Strip leading/trailing spaces and split into words
        words = s.strip().split()
        
        # Step 2: Reverse the list of words
        reversed_words = words[::-1]
        
        # Step 3: Join the words with a single space
        return ' '.join(reversed_words)
