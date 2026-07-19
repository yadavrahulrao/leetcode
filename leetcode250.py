
#1331. Rank Transform of an Array

class Solution(object):
    def arrayRankTransform(self, arr):
        rank = {}
        for i, num in enumerate(sorted(set(arr)), 1):
            rank[num] = i

        # Replace each element with its rank
        return [rank[num] for num in arr]
        
        
        