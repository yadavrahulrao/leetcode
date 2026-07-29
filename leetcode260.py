#495. Teemo Attacking

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        
       
        
        if not timeSeries:
            return 0

        total = 0
        end = 0

        for t in timeSeries:
            if t >= end:
                total += duration
            else:
                total += t + duration - end
            end = t + duration

        return total