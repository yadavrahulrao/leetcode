#283. Move Zeroes

class Solution(object):
    def moveZeroes(self, nums):
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0 :
                nums[j],nums[i] = nums[i],nums[j]
                i+= 1
        return nums

            

            
        
obj = Solution()
print(obj.moveZeroes([0,1,0,3,12]))

            
       
        