#1456. Maximum Number of Vowels in a Substring of Given Length
class Solution:
    def maxVowels(self, s, k):
        vowels = set("aeiou")

        # Count vowels in the first window
        count = sum(1 for ch in s[:k] if ch in vowels)
        ans = count

        # Slide the window
        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1

            if s[i - k] in vowels:
                count -= 1

            ans = max(ans, count)

        return ans

obj = Solution()
print(obj.maxVowels("abciiidef",3))
        