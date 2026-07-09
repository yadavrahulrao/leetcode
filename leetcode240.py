#435. Non-overlapping Intervals



class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: x[1])
        end = intervals[0][1]
        count = 0
        for i , j in intervals[1:]:
            if i >= end :
                end = j
            else:
                count += 1
        return count
            
            
        
        
obj = Solution()
print(obj.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
        
        