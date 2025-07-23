# You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

# Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

# Note:

# You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
# The transaction fee is only charged once for each stock purchase and sale.
 

# Example 1:

# Input: prices = [1,3,2,8,4,9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# - Buying at prices[0] = 1
# - Selling at prices[3] = 8
# - Buying at prices[4] = 4
# - Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
# Example 2:

# Input: prices = [1,3,7,5,10,3], fee = 3
# Output: 6
 



#greedy DP solution
# time complexity: O(n)
# space complexity: O(n)


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        hold = [0] * n
        free = [0] * n
        hold[0] = -prices[0]

        for i in range(1, n):
            hold[i] = max(hold[i - 1], free[i - 1] - prices[i])
            free[i] = max(free[i - 1], hold[i - 1] + prices[i] - fee)
        return free[-1]  




#space optimized greedy dp solution
# time complexity: O(n)
# space complexity: O(1)

# In the previous solution, we created two arrays of length n to record the maximum profits up to each day.

# However, if we look at the state transition equation:

# hold[i] = max(hold[i - 1], free[i - 1] - prices[i])
# free[i] = max(free[i - 1], hold[i - 1] + prices[i] - fee)
# We can see that the maximum profit up to day i (hold[i] or free[i]) only depends on the maximum profit up to day i - 1 (hold[i - 1] and free[i - 1]),
#  and we don't need to keep track of the profits from earlier days.

# Therefore, we can use only two variables hold and free to represent the maximum profits in the two states on the current day. 
# When we move to the next day (day i), we can simply update these two variables.

# hold = max(hold, free - prices[i])
# free = max(free, hold + prices[i] - fee)
# To avoid modifying hold before updating free, we can do the following:

# tmp = hold
# hold = max(hold, free - prices[i])
# free = max(free, tmp + prices[i] - fee)

# Algorithm
# Set free = 0 and hold = -prices[0] as the maximum profit for two status on day 0.

# Iterate from day 1 to day n - 1, on each day i:

# Set tmp = hold so that we record the maximum profit for holding a stock on day i - 1.
# Update hold to the larger of hold and free - prices[i].
# Update free to the larger of free and tmp + prices[i] - fee.
# Return free once the iteration ends.

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        hold = -prices[0]
        free = 0

        for i in range(1, n):
            tmp = hold
            hold = max(hold, free - prices[i])
            free = max(free, tmp + prices[i] - fee)
        return free
