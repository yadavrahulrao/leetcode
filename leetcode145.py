# 220. Contains Duplicate III
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0:
            return False

        bucket_size = valueDiff + 1
        buckets = {}

        def get_bucket_id(x):
            # Python's // already does floor division correctly
            return x // bucket_size

        for i, num in enumerate(nums):
            b = get_bucket_id(num)

            if b in buckets:
                return True

            # check neighbors
            if b - 1 in buckets and abs(num - buckets[b - 1]) <= valueDiff:
                return True
            if b + 1 in buckets and abs(num - buckets[b + 1]) <= valueDiff:
                return True

            buckets[b] = num

            # maintain sliding window
            if i >= indexDiff:
                old_bucket = get_bucket_id(nums[i - indexDiff])
                del buckets[old_bucket]

        return False
