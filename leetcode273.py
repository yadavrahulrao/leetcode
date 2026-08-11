#3254. Find the Power of K-Size Subarrays I

class Solution(object):
    def resultsArray(self, nums, k):
        result = []

        for i in range(len(nums) - k + 1):
            subarray = nums[i:i + k]

            valid = True

            for j in range(1, k):
                if subarray[j] != subarray[j - 1] + 1:
                    valid = False
                    break

            if valid:
                result.append(subarray[-1])
            else:
                result.append(-1)

        return result


obj = Solution()
print(obj.resultsArray([1, 2, 3, 4, 3, 2, 5], 3))