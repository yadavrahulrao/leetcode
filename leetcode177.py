#336. Palindrome Pairs
class Solution:
    def palindromePairs(self, words):
        def is_palindrome(s):
            return s == s[::-1]

        word_map = {word[::-1]: i for i, word in enumerate(words)}
        res = []

        for i, word in enumerate(words):
            n = len(word)
            for k in range(n + 1):
                left = word[:k]
                right = word[k:]

                # Case 1: left is palindrome, match reversed right
                if is_palindrome(left) and right in word_map:
                    j = word_map[right]
                    if j != i:
                        res.append([j, i])

                # Case 2: right is palindrome, match reversed left
                # k != n avoids duplicates when right is empty
                if k != n and is_palindrome(right) and left in word_map:
                    j = word_map[left]
                    if j != i:
                        res.append([i, j])

        return res


words = ["abcd","dcba","lls","s","sssll"]

s = Solution()
print(s.palindromePairs(words))