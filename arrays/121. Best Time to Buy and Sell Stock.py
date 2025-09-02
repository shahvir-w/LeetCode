class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        maxProfit = 0
        buyPrice = prices[0]

        for price in prices[1:]:
            if price < buyPrice:
                buyPrice = price

            maxProfit = max(maxProfit, price - buyPrice)

        return maxProfit 
        