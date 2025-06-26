#Maximum Product Subarray


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        max_prod = min_temp = max_temp = nums[0]

        for num in nums[1:]:
            if num < 0:
                min_temp, max_temp = max_temp, min_temp

            max_temp = max(num, max_temp * num)
            min_temp = min(num, min_temp * num)

            max_prod = max(max_prod, max_temp)

        return max_prod
