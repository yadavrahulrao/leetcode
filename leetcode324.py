#121. Best Time to Buy and Sell Stock


class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)

        # this fail when the last element is small .
        # list1 = []
        # min_val = min(prices)
        # for i in range(n):
        #     if prices[i] == min_val:
        #         s = prices[i:]
        # max_val = max(s)
        # return max_val - min_val

        # tle error 
        # max_pro = 0
        # for i in range(0,n):
        #     for j in range(i+1,n):
        #         if prices[j] > prices[i]:
        #             p = prices[j] - prices[i]
        #             max_pro = max(max_pro,p)
        # return max_pro

        max_pro = 0
        min_p = float("inf")
        for i in range(0,n):
            min_p = min(min_p,prices[i])
            max_pro = max(max_pro,prices[i] - min_p)

        return max_pro

            
obj = Solution()
print(obj.maxProfit([2,4,1]))
