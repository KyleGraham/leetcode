# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

# You may buy and sell one NeetCoin multiple times with the following restrictions:

# After you sell your NeetCoin, you cannot buy another one on the next day (i.e., there is a cooldown period of one day).
# You may only own at most one NeetCoin at a time.
# You may complete as many transactions as you like.

# Return the maximum profit you can achieve.

# Example 1:

# Input: prices = [1,3,4,0,4]

# Output: 6
# Explanation: Buy on day 0 (price = 1) and sell on day 1 (price = 3), profit = 3-1 = 2. 
# Then buy on day 3 (price = 0) and sell on day 4 (price = 4), profit = 4-0 = 4. Total profit is 2 + 4 = 6.

# Example 2:

# Input: prices = [1]

# Output: 0

#solution using dynamic programming top down with memoization
#time complexity: O(n) 
#space complexity: O(n)

#initialize dp as a hash, this will hold (index, buying) as the key and max profit as the value
#buying is a boolean value that indicates if we are buying or selling

#initialize a dfs function that takes in the index and buying boolean
#check if the index is out of bounds, if so return 0
#check if the key is in the dp hash, if so return the value
#initialize cooldown as the dfs of the next index and buying boolean
#check if we are buying
# if so, set buy to the dfs of the next index and not buying boolean minus the price at the index
# set the hash value of the max of buy and cooldown

#if not buying
# set sell to the dfs of the index + 2 and not buying boolean plus the price at the index since we made money
# set the hash value of the max of sell and cooldown
# return the hash value

#finally, return the dfs of index 0 and True
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #state: buying or selling?
        #if buy -> i + 1
        #if sell -> i + 2
        dp = {} #key=(i, buying) val=max_profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]
        
        return dfs(0, True)