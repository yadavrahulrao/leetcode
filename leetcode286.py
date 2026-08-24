#189. Rotate Array


class Solution(object):
    def rotate(self, nums, k):
        # list1 = []
        # list2 = []
        # for j in range(nums[0],nums[-k]):
        #     list2.append(j)
        
        # for i in range(nums[-k], len(nums)+1):
        #     list1.append(i)
        # return list1+list2 , nums


        k = k % len(nums)
        nums[:]= nums[-k:] + nums[:-k]
        return nums
            

obj = Solution()
print(obj.rotate([1,2,3,4,5,6,7],3))
        