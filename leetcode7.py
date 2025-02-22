#We are playing a game with the stones.
#  On each turn, we choose the heaviest two stones and smash them together.
#  Suppose the heaviest two stones have weights x and y with x <= y.
#  The result of this smash is:

import heapq
class Solution:
    def lastStoneWeight(self, stones):
        maxheap = [ -stone for stone in stones ]
        heapq.heapify(maxheap)
        while len(maxheap) >1:
            stone1 = -heapq.heappop(maxheap)
            stone2 = -heapq.heappop(maxheap)
            if stone1 != stone2 :
                heapq.heappush(maxheap,(stone2 - stone1))
        return -maxheap[0] if maxheap else 0
d = Solution()
stones = [2,7,4,1,8,1]
f = d.lastStoneWeight(stones)
print(f)
        