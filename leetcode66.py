#678. Valid Parenthesis String



class Solution:
    def checkValidString(self, s: str) -> bool:
        min , max = 0,0
        for c in s:
            if  c == "(":
                min , max = min + 1 ,max + 1
            
            elif c == ")":
                min , max = min - 1, max -1
            
            else :
                min , max = min - 1,max + 1

            if max < 0 :
                return False
            
            if  min < 0:
                min = 0
        return min == 0
            
                