#3942. Minimum Operations to Sort a Permutation


#53. Maximum Subarray
class Solution(object):
    def maxSubArray(self, nums):
        # n = len(nums)
        # maxi = float("-inf")
        # for i in range(0,n):
        #     sum = 0
        #     for j in range(i,n):
        #         sum = sum + nums[j]
        #         maxi = max(maxi,sum)
        # return maxi

        n = len(nums)
        maxi = float("-inf")
        sum = 0
        for i in range(0,n):
            sum = sum + nums[i]
            maxi = max(maxi,sum)
            if sum < 0 :
                sum = 0
        return maxi


obj = Solution()
print(obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
        
