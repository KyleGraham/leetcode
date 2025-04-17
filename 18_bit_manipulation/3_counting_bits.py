# Given an integer n, count the number of 1's in the binary representation of every number in the range [0, n].

# Return an array output where output[i] is the number of 1's in the binary representation of i.

# Example 1:

# Input: n = 4

# Output: [0,1,1,2,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100



#solution using a dp cache and iteration
#doesn't really actually use bit manipulation, just understanding the binary representation of numbers
#time complexity: O(n)
#space complexity: O(1)
#offset is basically the most significant digit, so it's at 1, 2, 4, 8, 16, 32, etc
#so for example, 5 is 101 in binary, so the most significant digit is 4
#we use dp to reduce repeat work
#basically dp[i] = 1 + dp[i - offset]
#so for example, dp[5] = 1 + dp[(5 - 4)=(1)] = 1 + 0 = 1
#and for every i, we check if it's equal to offset * 2, if it is we set offset to i

#0 0000 
#1 0001 = 1 + dp[i - offset]
#2 0010 = 1 + dp[i - offset]
#3 0011 = 1 + dp[i - offset]
#4 0100 = 1 + dp[i - offset]
#5 0101 = 1 + dp[i - offset]
#6 0110 = 1 + dp[i - offset]
#7 0111 = 1 + dp[i - offset]
#8 1000 = 1 + dp[i - offset]



class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]

        return dp