#485. Max Consecutive Ones

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        nums.append(0)
        count = 0
        list1 = []
        for i in nums:
            if i == 1 :
                count += 1
            if i == 0 :
                list1.append(count)
                count = 0 

        return max(list1)

obj = Solution()
print(obj.findMaxConsecutiveOnes([1,0,1,1,0,1]))

        