#  First Missing Positive


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # Step 1: Place each number in its correct position if possible
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct_index = nums[i] - 1
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
        
        # Step 2: Find the first location where the index doesn't match the value
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # Step 3: All numbers are in the correct place
        return n + 1
