# Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of
# a and b to make ( a OR b == c ). (bitwise OR operation).
# Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in 
# their binary representation.

 

# Example 1:



# Input: a = 2, b = 6, c = 5
# Output: 3
# Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)
# Example 2:

# Input: a = 4, b = 2, c = 7
# Output: 1
# Example 3:

# Input: a = 1, b = 2, c = 3
# Output: 0
 

# Constraints:

# 1 <= a <= 10^9
# 1 <= b <= 10^9
# 1 <= c <= 10^9


#using bit manipulation
#time complexity: O(n) where n is the input number
#space complexity: O(1) 

# (c & 1) gets the least significant bit of c.
# (a & 1) gets the least significant bit of a.


# Algorithm
# Initialize a variable answer as 0, which will be used to keep track of the
# minimum number of flips needed.

# Iterate over each bit of the binary representation of a, b, and c simultaneously:

# If (c & 1) = 0, update answer as answer += (a & 1) + (b & 1).

# If (c & 1) = 1, if both a & 1 and b & 1 equal 0, increment answer by 1.

# Shift all numbers to the right by a >>= 1, b >>= 1, c >>= 1. 
# If all numbers are equal to 0, return answer, otherwise, repeat steps 3 and 4.

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        while a or b or c:
            #c has a 1 in the least significant bit, so we check if
            #either a or b has a 1 in the least significant bit
            #if so, we don't need to flip anything
            #if not, we need to flip one of them to make c equal to 1
            if c & 1:
                if ((a & 1) or (b & 1)):
                    res += 0
                else:
                    res += 1
            else:
                #c has a 0 in the least significant bit
                #so we add the least significant bits of a and b to res
                res += (a & 1) + (b & 1)
            #shift all numbers to the right by 1
            a >>= 1
            b >>= 1
            c >>= 1
        return res
