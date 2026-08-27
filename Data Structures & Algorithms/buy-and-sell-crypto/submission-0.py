# Time: O(n), space: O(1), n = num of prices
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum, profit = 100, 0
        for price in prices:
            if price < minimum:
                minimum = price
            cur_profit = price - minimum
            if cur_profit > profit:
                profit = cur_profit
        return profit
                

        
        