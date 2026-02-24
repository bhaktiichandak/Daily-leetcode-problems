class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # Update minimum price seen so far
            min_price = min(min_price, price)

            # Calculate profit if sold today
            profit = price - min_price

            # Update maximum profit
            max_profit = max(max_profit, profit)

        return max_profit
       