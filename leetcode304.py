# #1423. Maximum Points You Can Obtain from Cards


# class Solution(object):
#     def maxScore(self, cardPoints, k):
#         n = len(cardPoints)
#         if n == k :
#             return sum(cardPoints)
#         count = 0 
#         for i in range(k + 1):
#             left = sum(cardPoints[:i])
#             right = sum(cardPoints[n-(k-i):])
#             total = left + right 
#             count = max(total,count)
#         return count

        

# obj = Solution()
# print(obj.maxScore([1,2,3,4,5,6,1],3))


class Solution:
    def maxScore(self, cardPoints, k) :
        n = len(cardPoints)

        # If we take all cards
        if k == n:
            return sum(cardPoints)

        total = sum(cardPoints)
        window_size = n - k

        # Sum of the first window
        window_sum = sum(cardPoints[:window_size])
        min_window = window_sum

        # Find minimum-sum window of size n-k
        for i in range(window_size, n):
            window_sum += cardPoints[i] - cardPoints[i - window_size]
            min_window = min(min_window, window_sum)

        return total - min_window
