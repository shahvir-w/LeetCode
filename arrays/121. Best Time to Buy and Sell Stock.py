class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # intuitive solution
        maxProfit = 0
        currentLowest = prices[0]

        for price in prices:
            if price <= currentLowest:
                currentLowest = price

            potentialProfit = price - currentLowest
            if p/otentialProfit >= maxProfit:
                maxProfit = potentialProfit
        
        return maxProfit

        #sliding window
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1
        return maxProfit