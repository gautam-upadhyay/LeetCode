class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # min_price = float('inf')
        # profit = 0

        # for price in prices:
        #     min_price = min(price, min_price)
        #     profit = max(profit, price - min_price)
        # return profit

        min_profit = float('inf')
        max_profit = 0

        # for i in range(len(prices)):
        #     min_profit = min(prices[i], min_profit)
        #     max_profit = max(max_profit, prices[i]- min_profit)

        for price in prices:
            # min_profit = min(price, min_profit)
            # max_profit = max(max_profit, price - min_profit)
            if price < min_profit:
                min_profit = price

            elif price - min_profit > max_profit:
                max_profit = price - min_profit

        return max_profit