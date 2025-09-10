class Solution(object):
    class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        currentLowestStock = 0

        for i in range(len(prices)):
            if prices[i] <= prices[currentLowestStock]:
                currentLowestStock = i
            profit = prices[i] - prices[currentLowestStock]

            if profit > maxProfit:
                maxProfit = profit

        return maxProfit
        