#905. Sort Array By Parity

class Solution(object):
    def sortArrayByParity(self, nums):
        list1 = []
        list2 = []
        for i in nums:
            if i % 2 == 0 :
                list1.append(i)
            else :
                list2.append(i)

        return list1+list2
                

obj = Solution()
print(obj.sortArrayByParity([3,1,2,4]))