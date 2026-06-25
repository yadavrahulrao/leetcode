#1752. Check if Array Is Sorted and Rotated

class Solution(object):
    def check(self, nums):
        s  = sorted(nums)
        n = len(nums)
        rot = []
        for i in range(n):
            r = s[i:] + s[:i]
            rot.append(r)
        
        if nums in rot :
            return True
        else :
            return False
        
    
    
obj = Solution()
print(obj.check([3,4,5,1,2]))
        
        