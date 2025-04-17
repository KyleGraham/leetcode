# Given two integers a and b, return the sum of the two integers without using the + and - operators.

# Example 1:

# Input: a = 1, b = 1

# Output: 2
# Example 2:

# Input: a = 4, b = 7

# Output: 11


#solution using bit manipulation
#time complexity: O(1)
#space complexity: O(1)


#need the mask due to python's handling of integers, they are not 32 bit

#doing ^ does the addition, but does not handle the carry
#so we do the & 1 to handle the carry, 
#mask = 0xFFFFFFFF
#max_int = 0x7FFFFFFF
#these handle pythons arbitrary large ints

#while b != 0:
#carry = (a & b) << 1
# a = (a ^ b) & mask
# b = carry & mask

#check if a is less than or equal to max_int
# if so return a
# else return ~(a ^ mask) a Xor the mask and negated

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        return a if a <= max_int else ~(a ^ mask)