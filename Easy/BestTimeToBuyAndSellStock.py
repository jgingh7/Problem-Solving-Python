# https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/572/
# Time: O(len(prices))
# Space: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        maxProfit = 0
        minPrice = prices[0]
        maxPrice = prices[0]
        
        for i in range(len(prices) - 1):
            if prices[i + 1] < minPrice:
                if maxPrice - minPrice > maxProfit:
                    maxProfit = maxPrice - minPrice
                minPrice = prices[i + 1]
                maxPrice = prices[i + 1]
            elif prices[i + 1] > maxPrice:
                maxPrice = prices[i + 1]
                
        if maxPrice - minPrice > maxProfit:
            maxProfit = maxPrice - minPrice
    
        return maxProfit