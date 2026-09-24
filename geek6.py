#Print GFG n times


n = int(input())
class Solution():
    def printGFG(self,n):
        list1 = []

        if n == 0 :
            return
        self.printGFG(n-1)
        print("GFG",end=" ")

        

obj = Solution()
obj.printGFG(n)
