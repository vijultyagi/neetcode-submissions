# T:O(n^2), S:O(1)
# Brute force
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        profit = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                if prices[j] > prices[i]:
                    profit = max(profit, prices[j] - prices[i])
        return profit
        