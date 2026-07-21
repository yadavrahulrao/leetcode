#796. Rotate String
class Solution:
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False
        
        return goal in (s + s)