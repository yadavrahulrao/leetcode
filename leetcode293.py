#768. Max Chunks To Make Sorted II

class Solution:
    def maxChunksToSorted(self, arr):
        sorted_arr = sorted(arr)

        chunks = 0
        s1 = 0
        s2 = 0

        for a, b in zip(arr, sorted_arr):
            s1 += a
            s2 += b

            if s1 == s2:
                chunks += 1

        return chunks

