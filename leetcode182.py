#227. Basic Calculator II
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        n = 0
        op = '+'

        for i , char in enumerate(s):
          if char.isdigit():
            n = n * 10 + int(char)

          if char in '+-*/' or i == len(s)-1:
            if op == '+':
              stack.append(n)
            elif op == '-':
              stack.append(-n)
            elif op == "*":
              stack.append(stack.pop()* n)
            elif op == '/' :
              stack.append(int(stack.pop()/ n))

            op = char
            n = 0
        return sum(stack)

cal = Solution()
s = "3+2*2"

print(cal.calculate(s))