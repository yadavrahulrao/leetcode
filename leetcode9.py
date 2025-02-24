#Given an integer array nums and an integer val, 
# remove all occurrences of val in nums in-place.
#  The order of the elements may be changed. 
# Then return the number of elements in nums which are not equal to val.

class Solution:
    def removeElement(self, nums, val):
        k = 0  # Pointer to place the next non-val element
        
        # Iterate over the array
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Place the non-val element in position k
                k += 1  # Increment k
        
        return k
