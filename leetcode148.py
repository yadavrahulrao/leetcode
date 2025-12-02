#406. Queue Reconstruction by Height
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort by height descending, k ascending
        people.sort(key=lambda x: (-x[0], x[1]))
        
        result = []
        
        # Step 2: Insert each person at index k
        for p in people:
            result.insert(p[1], p)
        
        return result
