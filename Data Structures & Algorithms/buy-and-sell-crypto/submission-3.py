# Time: O(n), space: O(1), n = num of prices
class Solution0:
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
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
           for j in  range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
        return max_profit



# Time: O(n), space: O(1), n = length of prices
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        if len(prices) <= 1:
            return 0

        i, j = 0, 1
        while i != len(prices) - 1 and j != len(prices):
            if prices[i] > prices[j]:
                i = j
                j += 1
                continue
            profit = prices[j] - prices[i]
            max_profit = max(profit, max_profit)
            j += 1 
        return max_profit    

        

        




#prices = [10, 8, 7, 5, 2]
#i = 0, j = 1 => prices[i] > prices[j], profit == -2 < max_profit = 0 => i += 1 => i == 1










