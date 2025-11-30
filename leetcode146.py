#747. Largest Number At Least Twice of Others
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        # Find index of the maximum value
        max_index = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[max_index]:
                max_index = i

        # Check if the max is at least twice every other number
        for i in range(len(nums)):
            if i != max_index and nums[max_index] < 2 * nums[i]:
                return -1

        return max_index
