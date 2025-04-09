# You are given an integer n representing the number of steps to reach the top of a staircase. 
# You can climb with either 1 or 2 steps at a time.

# Return the number of distinct ways to climb to the top of the staircase.

# Example 1:
# Input: n = 2
# Output: 2
# Explanation:
# 1 + 1 = 2
# 2 = 2

# Example 2:
# Input: n = 3
# Output: 3


#bottom up dynamic programming soluiton
#time complexity O(n)
#space complexity O(1)

#uses the fibonacci sequence to solve the problem
#the last two values of the sequence are always 1 and 1
#the next value is the sum of the last two values
#this is a bottom up dynamic programming solution
#initialize one and two to 1, the last two values of the sequence
#loop through n - 1 times, since we already have the last two values
#initialize temp to one, since we will be overriding it
#one is the second to last value of the sequence, two is the last value
#one is the sum of the last two values, two is the last value
#return one, since it is the last value of the sequence

class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1 #last 2 values of the sequence are always 1 and 1
        for i in range(n - 1):
            temp = one #temp so we don't override one
            one = one + two
            two = temp
        
        return one





#recursive solution
#time complexity O(2^n)
#space complexity O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(val):
            if val > n:
                return 0
            elif val == n:
                return 1
            else:
                return climb(val + 1) + climb(val + 2)
        return climb(0)