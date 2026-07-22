#3940. Limit Occurrences in Sorted Array

from collections import Counter
class Solution(object):
    def limitOccurrences(self, nums, k):
        cnt = Counter(nums)
        dct = dict(cnt)
        for i,j in dct.items():
            if j > k:
                dct[i] = k 
                
        result = list(Counter(dct).elements())
        fin = sorted(result)
        return fin
        
    
obj = Solution()
print(obj.limitOccurrences([29,35],2))
