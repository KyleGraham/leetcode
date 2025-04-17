# You are given a signed 32-bit integer x.

# Return x after reversing each of its digits. 
# After reversing, if x goes outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0 instead.

# Solve the problem without using integers that are outside the signed 32-bit integer range.

# Example 1:

# Input: x = 1234

# Output: 4321
# Example 2:

# Input: x = -1234

# Output: -4321
# Example 3:

# Input: x = 1234236467

# Output: 0


#solution using iteration
#time complexity: O(1)
#space complexity: O(1)

#essentially, we can reverse an integer by taking it and moding it by 10, getting the remainder
#we add that to the result, then divide the integer by 10, and multiplying the result by 10
#we repeat this until the integer is 0
#we also need to check for overflow, so we check if the result is greater than 2^31 - 1 or less than -2^31
#we do this by checking if the result is greater than the max int divided by 10 so the result doesn't overflow while checking
#we also check if the result is less than the min int divided by 10 so the result doesn't overflow while checking

class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648  # -2^31,
        MAX = 2147483647  #  2^31 - 1

        res = 0
        while x:
            digit = int(math.fmod(x, 10)) #this is needed cuz python dumb, -1 % 10 = -1 in python for some reason
            x = int(x / 10)               #also for this one, -1 // 10 = -1

            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0
            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0
            res = (res * 10) + digit

        return res