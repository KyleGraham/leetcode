# Given a 32-bit unsigned integer n, reverse the bits of the binary representation of n and return the result.

# Example 1:

# Input: n = 00000000000000000000000000010101

# Output:    2818572288 (10101000000000000000000000000000)
# Explanation: Reversing 00000000000000000000000000010101, 
# which represents the unsigned integer 21, gives us 10101000000000000000000000000000 which represents the unsigned integer 2818572288.


#solution using bit manipulation
##time complexity: O(1)
##space complexity: O(1)

#initialize res as 0
#loop through i in range(32)
#initialize bit as n shifted by the right by i and bitwise and with 1
#add the bit shifted to the left by 31 - i to res
#return res

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += (bit << (31 - i))
        return res