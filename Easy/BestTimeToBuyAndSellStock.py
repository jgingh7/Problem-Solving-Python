# https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/572/
# Time: O(len(prices))
# Space: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        maxPrice = minPrice = prices[0]
        
        for i in range(len(prices) - 1):
            if prices[i + 1] < minPrice:
                maxProfit = max(maxProfit, maxPrice - minPrice)
                maxPrice = minPrice = prices[i + 1]
            elif prices[i + 1] > maxPrice:
                maxPrice = prices[i + 1]
            
        maxProfit = max(maxProfit, maxPrice - minPrice)
        
        return maxProfit