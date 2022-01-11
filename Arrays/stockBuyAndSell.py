from typing import List
"""
    You can not sell before you buy
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <1:
            return 0
        min_price, max_profit = prices[0], 0
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price # profit if sold at curr elem.
            max_profit = max(max_profit, profit)
        return max_profit

result = Solution()
result.maxProfit([7, 1, 5, 3, 6, 4])