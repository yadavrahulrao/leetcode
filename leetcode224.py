#456. 132 Pattern

class Solution(object):
    def find132pattern(self, nums):
        res = []
        neg = float('-inf')
        for i in reversed(nums):
            if i < neg :
                return True
            while res and i > res[-1]:
                neg = res.pop()
            res.append(i)
            
        return False
                
            
                    
obj = Solution()
print(obj.find132pattern([3,1,4,2]))
