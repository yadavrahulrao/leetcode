#Given an array of integers nums sorted in non-decreasing order,
#  find the starting and ending position of a given target value.
class Solution(object):
    def searchRange(self, nums, target):
        def lower(nums , target):
            low= 0
            high = len(nums) -1
            while low<= high :
                mid = (low+ high)//2
                if nums[mid] < target :
                    low = mid +1
                else :
                    high = mid -1
            return low
        def higher (nums, target):
            low = 0
            high = len(nums) -1
            while low<= high:
                mid = (low+high)//2
                if nums[mid]<= target:
                    low = mid +1
                else :
                    high = mid -1
            return high 

        lower_index = lower(nums,target)
        higher_index = higher(nums,target)   
        if lower_index <= higher_index :
            return [lower_index,higher_index]
        else :
            return[-1,-1]
nums = [5,7,7,8,8,10]
target = 8
s = Solution()
print(s.searchRange(nums,target))
