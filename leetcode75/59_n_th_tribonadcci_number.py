
# The Tribonacci sequence Tn is defined as follows: 

# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

# Given n, return the value of Tn.

 

# Example 1:

# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
# Example 2:

# Input: n = 25
# Output: 1389537
 

# Constraints:

# 0 <= n <= 37
# The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.

#solution using 1d dynamic programming
#time complexity: O(n)
#space complexity: O(n)

#essentially, initialize an array of zeroes with the size of 38 since max n is 37
#intialize index 0 as 0, index 1 as 1, and index 2 as 1
#then loop and fill the array from index 3 to n
#then return arr[n]

class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [0] * 38
        arr[0] = 0
        arr[1] = 1
        arr[2] = 1

        for i in range(3, n + 1):
            arr[i] = arr[i-1] + arr[i-2] + arr[i-3]
        return arr[n]
        