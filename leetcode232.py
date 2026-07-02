#241. Different Ways to Add Parentheses

class Solution(object):
    def diffWaysToCompute(self, expression):
        res = []
        for i , j in enumerate(expression):
            if j in "+-*":
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for l in left:
                    for r in right:
                        if j == "+":
                            res.append(l+r)
                        elif j == "-":
                            res.append(l-r)
                        else :
                            res.append(l*r)
        if not res :
            res.append(int(expression))
        return res
        
obj = Solution()
print(obj.diffWaysToCompute("2-1-1"))
        