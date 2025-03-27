#brute force
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            r = len(prices) - 1
            while i < r:
                profit = max(profit, prices[r] - prices[i])
                r -= 1
        return profit
      
      
#two pointer (sliding window)
#start 1 pointer at start and other pointer at start + 1
#right pointer checks if the value is lower than the left pointer for a buy value
# checks if the right pointer value is greater than the left pointer for a sell value
# if it is, calculates the sell value
# if not, buy price is lower than current, set the left pointer to the right pointer and increments the right pointer

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
      l, r = 0, 1
      maxP = 0

      while r < len(prices):
          if prices[l] < prices[r]:
              profit = prices[r] - prices[l]
              maxP = max(maxP, profit)
          else:
              l = r
          r += 1
      return maxP