# You are given an integer array coins representing coins of different denominations 
# (e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.

# Return the fewest number of coins that you need to make up the exact target amount. 
# If it is impossible to make up the amount, return -1.

# You may assume that you have an unlimited number of each coin.

# Example 1:
# Input: coins = [1,5,10], amount = 12
# Output: 3
# Explanation: 12 = 10 + 1 + 1. Note that we do not have to use every kind coin available.

# Example 2:
# Input: coins = [2], amount = 3
# Output: -1
# Explanation: The amount of 3 cannot be made up with coins of 2.

# Example 3:
# Input: coins = [1], amount = 0
# Output: 0
# Explanation: Choosing 0 coins is a valid way to make up 0.

# bottom up dynamic programming solution
# time complexity O(n * t) where n is len of coins and t is the amount
# space complexity O(t)

#basically we fill a cache with the amount of coins to get to each amount from 1 to amount

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1) # 0 to amount. amount + 1 acts as a max val
        dp[0] = 0
        #calculate the amount of coins needed to get the amounts
        #1 to amount
        #use amount + 1 since indexes
        for a in range(1, amount + 1):
            #check every coin for the fewest num of coins
            for c in coins:
                #if not negative (amount - coin)
                if a - c >= 0:
                    #set the cache dp value to the min of the cur val and 
                    #1 + the cache value of the amount - coin
                    dp[a] = min(dp[a], 1 + dp[a - c])
        #return the cache amount if its not the default, else return -1
        return dp[amount] if dp[amount] != amount + 1 else -1
