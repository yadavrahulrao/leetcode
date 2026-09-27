# n = int(input())
# list1 = []
# for i in range(n,0,-1):
#     list1.append(i)
    
# print(list1)


#Print n to 1 Without Loop
class Solution:
    def printNos(self, n: int) -> None:
        # Code here
        # if n == 0 :
        #     return 
        # self.printNos(n=n-1)
        # print(n,end=" ")

        if n != 0:
            print(n,end=" ")
            self.printNos(n=n-1)
        if n == 0 :
            return

obj = Solution()
obj.printNos(5)