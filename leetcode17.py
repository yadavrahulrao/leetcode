#Maximum Sum of 3 Non-Overlapping Subarrays


class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        
        # Step 1: Compute sum of each window of size k
        window_sum = [0] * (n - k + 1)
        curr_sum = sum(nums[:k])
        window_sum[0] = curr_sum
        for i in range(1, len(window_sum)):
            curr_sum += nums[i + k - 1] - nums[i - 1]
            window_sum[i] = curr_sum

        # Step 2: Build left array of best window starts
        left = [0] * len(window_sum)
        best = 0
        for i in range(len(window_sum)):
            if window_sum[i] > window_sum[best]:
                best = i
            left[i] = best

        # Step 3: Build right array of best window starts
        right = [0] * len(window_sum)
        best = len(window_sum) - 1
        for i in range(len(window_sum) - 1, -1, -1):
            if window_sum[i] >= window_sum[best]:
                best = i
            right[i] = best

        # Step 4: Try all middle intervals and track max sum
        max_total = 0
        result = [-1, -1, -1]
        for j in range(k, len(window_sum) - k):
            i = left[j - k]
            l = right[j + k]
            total = window_sum[i] + window_sum[j] + window_sum[l]
            if total > max_total:
                max_total = total
                result = [i, j, l]

        return result
