#789. Escape The Ghosts

class Solution:
    def escapeGhosts(self, ghosts, target):
        tx, ty = target
        return all(
            abs(x - tx) + abs(y - ty) > abs(tx) + abs(ty)
            for x, y in ghosts
        )