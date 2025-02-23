#Remove Duplicates from Sorted Array


class Solution:
    def removeDuplicates(self, nums):
        if not nums :
            return 0
        unique_index = 1 
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[unique_index] = nums[i]
                unique_index += 1
        return unique_index
nums1 = [1, 1, 2]
solution = Solution()
k1 = solution.removeDuplicates(nums1)
expectedNums1 = [1, 2]
assert k1 == len(expectedNums1)
for i in range(k1):
    assert nums1[i] == expectedNums1[i]
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
expectedNums2 = [0, 1, 2, 3, 4]
k2 = solution.removeDuplicates(nums2)
assert k2 == len(expectedNums2)
for i in range(k2):
    assert nums2[i] == expectedNums2[i]

print("All assertions passed!")
