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
                

        








# Brute force 
# Time: O(n ** 2), space: O(1), n = length of prices
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
           for j in  range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
        return max_profit















