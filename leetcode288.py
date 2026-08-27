#985. Sum of Even Numbers After Queries


class Solution:
    def sumEvenAfterQueries(self, nums, queries):
        even_sum = sum(x for x in nums if x % 2 == 0)
        result = []

        for val, i in queries:
            old = nums[i]

            if old % 2 == 0:
                even_sum -= old

            nums[i] += val

            if nums[i] % 2 == 0:
                even_sum += nums[i]

            result.append(even_sum)

        return result

