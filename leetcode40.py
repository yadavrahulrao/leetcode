#Continuous Subarray Sum


class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        mod_map = {0: -1}  # Maps mod value to its earliest index
        prefix_sum = 0

        for i, num in enumerate(nums):
            prefix_sum += num
            mod = prefix_sum % k if k != 0 else prefix_sum  # Handle k == 0 safely

            if mod in mod_map:
                if i - mod_map[mod] >= 2:  # Ensure subarray length at least 2
                    return True
            else:
                mod_map[mod] = i  # Store earliest occurrence of this mod

        return False
