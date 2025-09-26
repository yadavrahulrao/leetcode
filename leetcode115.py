#30. Substring with Concatenation of All Words
from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words or not words[0]:
            return []

        word_len = len(words[0])
        num_words = len(words)
        window_size = word_len * num_words
        word_count = Counter(words)
        result = []

        for i in range(word_len):  # Try all possible word alignments
            left = i
            right = i
            curr_count = Counter()

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in word_count:
                    curr_count[word] += 1

                    # Shrink window from the left if word is too frequent
                    while curr_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        curr_count[left_word] -= 1
                        left += word_len

                    # If window matches all words exactly
                    if right - left == window_size:
                        result.append(left)
                else:
                    # Reset the counters and move left pointer
                    curr_count.clear()
                    left = right

        return result
