#229. Majority Element II
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # 1. Find potential candidates
        cand1 = cand2 = None
        count1 = count2 = 0
        
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = num
                count1 = 1
            elif count2 == 0:
                cand2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        # 2. Verify candidates
        result = []
        if nums.count(cand1) > len(nums) // 3:
            result.append(cand1)
        if cand2 is not None and nums.count(cand2) > len(nums) // 3:
            result.append(cand2)
        
        return result
