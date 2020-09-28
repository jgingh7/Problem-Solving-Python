#https://leetcode.com/problems/coin-change/
#Time: O(coin.legnth * amount)
#Space: O(amount)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort() #for average time complexity optimization
        dp = [0] + [(amount + 1) for i in range(amount)] # there cannot be coins larger than amount + 1 (if amount is 10, max number of coins is 10)
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
                    #dp[i] represents the minimum amount of coins to make i
                    #plus 1 is to represent having one coin after checking through the i-coin>=0 statement
                else:
                    break
        if dp[-1] == amount + 1:
            return -1
        return dp[-1]