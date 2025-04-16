# You are given an integer array digits, where each digits[i] is the ith digit of a large integer. 
# It is ordered from most significant to least significant digit, and it will not contain any leading zero.

# Return the digits of the given integer after incrementing it by one.

# Example 1:

# Input: digits = [1,2,3,4]

# Output: [1,2,3,5]
# Explanation 1234 + 1 = 1235.

# Example 2:

# Input: digits = [9,9,9]

# Output: [1,0,0,0]

#solution using iteration
#time complexity: O(n)
#space complexity: O(1)

#loop through the digits in reverse order
#check if the digit is 9
# if so, set the digit to 0 
# else, increment the digit by 1 and break

#check if the first character is a 0
# if so, insert 1 at the beginning of the digits
#return digits

#we were given that there is never leading zeroes


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = False
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                carry = True
            else:
                digits[i] += 1
                carry = False
                break
        if carry:
            digits.insert(0, 1)
        return digits