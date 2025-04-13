# You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc)
# and an integer amount representing a target amount of money.

# Return the number of distinct combinations that total up to amount. If it's impossible to make up the amount, return 0.

# You may assume that you have an unlimited number of each coin and that each value in coins is unique.

# Example 1:
# Input: amount = 4, coins = [1,2,3]
# Output: 4
# Explanation:
# 1+1+1+1 = 4
# 1+1+2 = 4
# 2+2 = 4
# 1+3 = 4

# Example 2:
# Input: amount = 7, coins = [2,4]
# Output: 0



#solution using dynamic programming bottom up
#time complexity: O(n * a) where n is len of coins and a is given amount
#space complexity: O(n * a) where n is len of coins and a is given amount

#initialize dp as a 2d array of 0s with len(coins) + 1 and amount + 1
#the first row is all 1s since there is one way to make 0 amount
#loop through the array 1 to amount + 1
#loop through coins in reverse order (len(coins)) -1, -1, -1
#for each amount, set the current index to the index below
#and if the amount minus the coin is greater than or equal to 0
#add the index to the right by the amount - coin
#return the top left index, which is the number of ways to make the amount

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]
        dp[0] = [1] * (len(coins) + 1)

        for a in range(1, amount + 1):
            for i in range(len(coins) -1, -1, -1):
                dp[a][i] = dp[a][i + 1]
                if a - coins[i] >= 0:
                    dp[a][i] += dp[a - coins[i]][i]
        return dp[amount][0]
      
      
      
#space optimized
#initialize dp as [0] * (amount + 1)
#we only keep track of the row below the current row, which dp represents
#set dp[0] to 1 since there is one way to make 0 amount
#loop through the coins in reverse order
#add to dp[a] by the value of dp[a - coins[i]] if the coin is less than or equal to a, else 0

#return dp[amount], which is the number of ways to make the amount

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins) - 1, -1, -1):
            for a in range(1, amount + 1):
                dp[a] += dp[a - coins[i]] if coins[i] <= a else 0
        return dp[amount]