# A non-cyclical number is an integer defined by the following algorithm:

# Given a positive integer, replace it with the sum of the squares of its digits.
# Repeat the above step until the number equals 1, or it loops infinitely in a cycle which does not include 1.
# If it stops at 1, then the number is a non-cyclical number.
# Given a positive integer n, return true if it is a non-cyclical number, otherwise return false.

# Example 1:
# Input: n = 100
# Output: true
# Explanation: 1^2 + 0^2 + 0^2 = 1

# Example 2:
# Input: n = 101
# Output: false


#solution using fast and slow pointers (tortoise and hare)
#time complexity: O(log n) where n is the number of digits in the number
#space complexity: O(1)

#can do something like counting loops to break out of the loop if it's a cyclical number
#but better way is to do tortoise and hare

#essentially we want to find the sum of the squares of the digits
#then we want to check if the sum is equal to 1
#if its not, we repeat and try again
#if it cycles infinitely, its a cyclical number return false

#initialize slow as n
#initialize fast as the sum of squares of n
#while slow is not equal to fast
#initialize fast as the sum of squares of fast
#initialize fast as the sum of squares of fast
#initialize slow as the sum of squares of slow
#return true if fast is equal to 1, else false

#sumOfSquares function
#initialize total as 0
#loop through the digits in str(n), that way we can treat it as an array
#add the square of the digit to total
#return total


class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.sumOfSquares(n)
        while slow != fast:
            fast = self.sumOfSquares(fast)
            fast = self.sumOfSquares(fast)
            slow = self.sumOfSquares(slow)
        return True if fast == 1 else False

    def sumOfSquares(self, n):
        total = 0
        for c in str(n):
            total += int(c) ** 2
        return total