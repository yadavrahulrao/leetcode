#453. Minimum Moves to Equal Array Elements


class Solution:
    def minMoves(self, nums):
        minimum = min(nums)

        return sum(num - minimum for num in nums)