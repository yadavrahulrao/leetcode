#125. Valid Palindrome


class Solution:
    def isPalindrome(self, s: str) -> bool:

      pal = ''.join(ch.lower() for ch in s if ch.isalnum())

      return pal == pal[::-1]
        