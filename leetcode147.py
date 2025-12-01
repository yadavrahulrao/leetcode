#56. Merge Intervals
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort intervals by start time
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        
        for interval in intervals:
            # If no interval in merged OR no overlap → append
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Overlapping intervals → merge them
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
