# 2149. Rearrange Array Elements by Sign

class Solution(object):
    def rearrangeArray(self, nums):
        list1 = []
        list2 = []
        for i in nums:
            if i < 0 :
                list1.append(i)
            if i >= 0 :
                list2.append(i)

        res = [x for j in zip(list2,list1) for x in j]

        return res


obj = Solution()
print(obj.rearrangeArray([-1,1]))
        