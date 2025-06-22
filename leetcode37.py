# Moves Zeros

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None. Do not return anything, modify nums in-place instead.
        """
        non_zero_pos = 0  # Position to place the next non-zero element

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_pos], nums[i] = nums[i], nums[non_zero_pos]
                non_zero_pos += 1
