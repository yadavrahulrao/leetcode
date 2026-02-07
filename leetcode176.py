#65. Valid Number

class Solution:
    def isNumber(self, s: str) -> bool:
        digit = False 
        dot = False
        exp = False
        d_a_exp = True
        for i , c in enumerate(s):
          if c.isdigit():
            digit = True
            if exp:
              d_a_exp = True
          
          elif c in ['+','-']:
            if i!= 0 and s[i-1] not in ['e','E']:
              return False
          
          elif c == '.':
            if dot or exp :
              return False
            dot = True
          
          elif c in ['e','E']:
            if exp or not digit :
              return False 
            exp = True
            d_a_exp = False

          else :
            return False

        return digit and d_a_exp

s = "0"
x = Solution()
print(x.isNumber(s))
