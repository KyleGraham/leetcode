# You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.


# Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

# In a tiling, every square must be covered by a tile. Two tilings are different if and only if 
# there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

 

# Example 1:


# Input: n = 3
# Output: 5
# Explanation: The five different ways are shown above.
# Example 2:

# Input: n = 1
# Output: 1
 

# Constraints:

# 1 <= n <= 1000


#solution using 1d dynamic programming
#time complexity: O(n)
#space complexity: O(n)


# Algorithm

# We'll start from f(n) and then dive all the way down to the base cases, f(1), f(2), and p(2).
# Use the same definition for f and p from the Overview section
# f(k): The number of ways to fully cover a board of width k
# p(k): The number of ways to partially cover a board of width k
# Recursion calls will use the results of subproblems and base cases to help us get the final result, f(n).
# The stop condition for the recursive calls is when k reaches a base case (i.e. k<=2).
# Values for the base cases will be directly returned instead of making more recursive calls.
# f(1)=1
# f(2)=2
# p(2)=1
# To avoid repeated computations, we will use 2 hashmaps (f_cache and p_cache) to store calculated values for f and p. 
# In Python, the built-in @cache wrapper will automatically maintain these hashmaps for us.
# If k is greater than 2, then we will make recursive calls to f and p according to the transition function:
# f(k)=f(k−1)+f(k−2)+2∗p(k−1)
# p(k)=p(k−1)+f(k−2)
# f(n) will be returned once all recursive calls are finished.


class Solution:
    def numTilings(self, n: int) -> int:
        mod = 1_000_000_007

        @cache
        def p(n):
            if n == 2:
                return 1
            return (p(n - 1) + f(n - 2)) % mod
        
        @cache
        def f(n):
            if n <= 2:
                return n
            return (f(n - 1) + f(n - 2) + 2 * p(n - 1)) % mod
        
        return f(n)
