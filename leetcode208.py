#122. Best Time to Buy and Sell Stock II
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        n = len(prices)
        
        # for i in range(len(prices)):
        for i,j in zip(range(0,n-1),range(1,n)):
            if prices[i] < prices[j] :
              res += prices[j] - prices[i]

        return res 

s = Solution()
d = s.maxProfit([1,2,3,4,5])
print(d)
              
