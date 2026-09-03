#821. Shortest Distance to a Character





class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        positions = [i for i, ch in enumerate(s) if ch == c]

        return [
            min(abs(i - p) for p in positions)
            for i in range(len(s))
        ]
    
