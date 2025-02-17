# . Search in Rotated Sorted Array


class Solution(object):
    def search(self, nums , target):
        low = 0
        high = len(nums) -1
        while low<= high :
            mid = (low+high)//2
            if nums[mid] == target :
                return mid 
            
            if nums[low] <= nums[mid] :
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else :
                    low = mid +1
            else :
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else :
                    high  = mid - 1
        return - 1
        
nums = [1,2,3,4,5,6,7]
target = 4
s = Solution()
print(s.search(nums,target))