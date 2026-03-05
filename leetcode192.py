#698. Partition to K Equal Sum Subsets
class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
          return False

        target = total // k
        nums.sort(reverse=True)

        used = [False] * len(nums)

        def backtrack(start, k, curr_sum):
            if k == 1:
                return True

            if curr_sum == target:
                return backtrack(0, k - 1, 0)

            for i in range(start, len(nums)):
                if used[i] or curr_sum + nums[i] > target:
                    continue

                used[i] = True

                if backtrack(i + 1, k, curr_sum + nums[i]):
                    return True

                used[i] = False

            return False

        return backtrack(0, k, 0)