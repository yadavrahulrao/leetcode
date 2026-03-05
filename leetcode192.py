#698. Partition to K Equal Sum Subsets
class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        
        total = sum(nums)
        if total % k != 0:
            return False
        
        target = total // k
        nums.sort(reverse=True)

        buckets = [0] * k

        def backtrack(index):
            if index == len(nums):
                return True

            for i in range(k):
                if buckets[i] + nums[index] <= target:
                    buckets[i] += nums[index]

                    if backtrack(index + 1):
                        return True

                    buckets[i] -= nums[index]

                # pruning: avoid same state
                if buckets[i] == 0:
                    break

            return False

        return backtrack(0)