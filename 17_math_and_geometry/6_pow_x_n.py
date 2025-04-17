
# Pow(x, n) is a mathematical function to calculate the value of x raised to the power of n (i.e., x^n).

# Given a floating-point value x and an integer value n, implement the myPow(x, n) function, which calculates x raised to the power n.

# You may not use any built-in library functions.

# Example 1:

# Input: x = 2.00000, n = 5

# Output: 32.00000
# Example 2:

# Input: x = 1.10000, n = 10

# Output: 2.59374
# Example 3:

# Input: x = 2.00000, n = -3

# Output: 0.12500

#can optimize because of the idea that 
#2^5 * 2^5 = 2^10
#optimal Solution using recursion
#time complexity O(log n)
#space complexity O(log n) for recursion stack

#call the helper function with (x, abs(n))
#return res if n >= 0 else 1 / res to handle negatives

#helper function, takes in x and n
#check if n is 0, if so return 1
#check if x is 0, if so return 0
#call the helper function with x * x and n // 2 basicaly squaring the number and reducing the exponent by half
#check if n is odd, if so return x * res else return res


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 0:
                return 1
            if x == 0:
                return 0
            res = helper(x * x, n // 2)
            return x * res if n % 2 else res

        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res




#brute force solution
#time complexity: O(n)
#space complexity: O(1)

#if n is 0, return 1
#if n is negative, return 1 / x^n
#else return x^n


class Solution:
    def myPow(self, x: float, n: int) -> float:
        total = x
        if n == 0:
            return float(1)
        for i in range(1, abs(n)):
            total *= x
        if n < 0:
            total = 1 / total
        return total