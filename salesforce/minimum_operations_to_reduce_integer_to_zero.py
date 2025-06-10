# You are given a positive integer n, you can do the following operation any number of times:

# Add or subtract a power of 2 from n.
# Return the minimum number of operations to make n equal to 0.

# A number x is power of 2 if x == 2i where i >= 0.

 

# Example 1:

# Input: n = 39
# Output: 3
# Explanation: We can do the following operations:
# - Add 20 = 1 to n, so now n = 40.
# - Subtract 23 = 8 from n, so now n = 32.
# - Subtract 25 = 32 from n, so now n = 0.
# It can be shown that 3 is the minimum number of operations we need to make n equal to 0.
# Example 2:

# Input: n = 54
# Output: 3
# Explanation: We can do the following operations:
# - Add 21 = 2 to n, so now n = 56.
# - Add 23 = 8 to n, so now n = 64.
# - Subtract 26 = 64 from n, so now n = 0.
# So the minimum number of operations is 3.

#solution using bitwise operations
#time complexity O(logn)
#space complexity O(1)


# Take a look at the binary of n:

# If there is an alone 1, like ..00001,
# it takes at leat one operation to remove.
# and we can remove it in one operation.
# So we do res++ and n >>= 2,
# remove two last bits.

# If there are multiple 1s, like ..0000111,
# we can't remove them in one single operation,
# so it takes at least two operation to remove,
# For example of ..0000111
# we can add 1 and then remove 1000.
# So we do n++ and remove the last bit 0.


# Explanation
# By this stratagy in intuition,
# we only need to take care of the the continuous 1 in binary of n.
# If it's single 1, res += 1
# If it's multiple 1s, res += 2


#for 39
# 39 two
# 40 1 two-2
# 40 one
# 20 1 one-2
# 20 one
# 10 1 one-2
# 10 one
# 5 1 one-2
# 5 three
# 1 2 three-2
# 1 three
# 0 3 three-2

#for 54
# 54 one
# 27 0 one-2
# 27 two
# 28 1 two-2
# 28 one
# 14 1 one-2
# 14 one
# 7 1 one-2
# 7 two
# 8 2 two-2
# 8 one
# 4 2 one-2
# 4 one
# 2 2 one-2
# 2 one
# 1 2 one-2
# 1 three
# 0 3 three-2




class Solution:
    def minOperations(self, n: int) -> int:
        res = 0
        while n > 0:
            if n % 2 == 0:
                n >>= 1
            elif (n & 2) > 0:
                n += 1
                res += 1
            else:
                res += 1
                n >>= 2
        return res
    


#non bitwise solution, similar to what i was trying to do originally
#has worse space complexity since you need to have the powers array
#time complexity O(log(n))
#space complexity O(log(n))

#basically you make an array of the powers of 2 for range logn + 2, which keeps it from getting too big for a given n
#then while n
#find the closest by taking the minimum of powers with the key of abs(n - val)
#make n the abs of n - closest
#increment operations
#return operations

class Solution:
    def minOperations(self, n: int) -> int:

        pows = [1 << i for i in range(int(log2(n))+2)]
        ops = 0

        while n:
            closest = min(pows, key=lambda p: abs(n-p))
            n = abs(n-closest)
            ops += 1

        return ops