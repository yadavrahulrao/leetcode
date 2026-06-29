#593. Valid Square

import math
class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        lst = []
        dist1 = ((p2[0]-p1[0])** 2  + (p2[1]-p1[1])**2)
        lst.append(dist1)
        dist2 = ((p3[0]-p2[0])** 2  + (p3[1]-p2[1])**2)
        lst.append(dist2)
        dist3 = ((p4[0]-p3[0])** 2  + (p4[1]-p3[1])**2)
        lst.append(dist3)
        dist4 = ((p1[0]-p4[0])** 2  + (p1[1]-p4[1])**2)
        lst.append(dist4)
        dist5 = ((p3[0]-p1[0])** 2  + (p3[1]-p1[1])**2)
        lst.append(dist5)
        dist6 = ((p4[0]-p2[0])** 2  + (p4[1]-p2[1])**2)
        lst.append(dist6)
        
        s = set(lst)
        # return lst
        
        if len(s) == 2  and 0 not in s :
            return True 
        return False
        
        
        
         
obj = Solution()
print(obj.validSquare(p1 = [0,0], p2 = [1,1], p3 = [0,0], p4 = [0,0]))
        
        