#75. Sort Colors

class Solution(object):
    def sortColors(self, nums):


        #quick sort
        
        # if len(nums) <= 1:
        #     return nums
        # pivot = nums[(len(nums))//2]
        # left = [x for x in nums if x < pivot]
        # middle = [x for x in nums if x == pivot]
        # right = [x for x in nums if x > pivot]
        # return left + middle + right
        

        #bubble sort

        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums

obj = Solution()
print(obj.sortColors([0,1,2,0,1,1,1,0,2,1]))

