from collections import defaultdict
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_idx = 0
        sell_idx = 0
        print(prices[buy_idx],prices[sell_idx])
        
        for i in range(len(prices)):
            if prices[i] < prices[buy_idx]:
                buy_idx = i
                sell_idx = i
                max_profit = max(max_profit,prices[sell_idx] - prices[buy_idx])
            
            elif prices[i] > prices[sell_idx]:
                sell_idx = i
                max_profit = max(max_profit,prices[sell_idx] - prices[buy_idx])

            print(prices[i],  prices[buy_idx],prices[sell_idx])
        return max(max_profit,0)