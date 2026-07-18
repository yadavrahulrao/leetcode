#1207. Unique Number of Occurrences

from collections import Counter
class Solution(object):
    def uniqueOccurrences(self, arr):
        cnt = Counter(arr)
        dct = dict(cnt)
        lst1 = list(dct.values())
        st = set(lst1)
        lst2 = list(st)
        if len(lst1) == len(lst2):
            return True
        else:
            return False
    
    
obj = Solution()
print(obj.uniqueOccurrences([1,2,2,1,1,3]))
        
        
        