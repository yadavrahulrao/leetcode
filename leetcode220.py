#345. Reverse Vowels of a Strings

class Solution(object):
    def reverseVowels(self, s):
        vowels = "aeiouAEIOU"
        index = [i for i , j in enumerate(s) if j in vowels]
        reverse = index[::-1]
        
        ele = [s[k] for k in index]
        text = list(s)
        for n , m in zip(reverse,ele):
          if n  < len(text):
            text[n] = m
        res = "".join(text)
        return res

obj = Solution()
print(obj.reverseVowels("IceCreAm"))
        