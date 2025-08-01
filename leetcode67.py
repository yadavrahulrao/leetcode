#496. Next Greater Element I



from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}

        # Iterate nums2 in reverse to find next greater elements
        for num in reversed(nums2):
            # Pop elements from stack that are less than or equal to current num
            while stack and stack[-1] <= num:
                stack.pop()

            # If stack is not empty, the top is the next greater element
            next_greater[num] = stack[-1] if stack else -1

            # Push current number onto the stack
            stack.append(num)

        # Build result for nums1 using the next_greater dictionary
        return [next_greater[num] for num in nums1]
