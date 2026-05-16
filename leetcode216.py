#2951. Find the Peaks
class Solution(object):
    def findPeaks(self, mountain):
        lst = []
        n = len(mountain)
        for i in range(1,n-1):
          if mountain[i-1] < mountain[i] > mountain[i+1] :
            lst.append(i)
        return lst

s = Solution()
print(s.findPeaks([2,4,4]))
        