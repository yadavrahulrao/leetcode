#1. Two Sum


class Solution(object):
    def twoSum(self, nums, target):
        list1 = []
        n = len(nums)
        for i in range(n):
            s = target - nums[i]
            for j in range(i+1,n):
                if s == nums[j]:
                    list1.append(i)
                    list1.append(j)
        return list1


obj = Solution()
print(obj.twoSum([3,2,4],6)) 


        