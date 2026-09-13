#1897. Redistribute Characters to Make All Strings Equal

class Solution:
    def makeEqual(self, words):
        n = len(words)
        count = [0] * 26

        for word in words:
            for ch in word:
                count[ord(ch) - ord('a')] += 1

        for freq in count:
            if freq % n != 0:
                return False

        return True
