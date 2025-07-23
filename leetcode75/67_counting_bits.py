# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
# ans[i] is the number of 1's in the binary representation of i.

 

# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# Example 2:

# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
 

# Constraints:

# 0 <= n <= 105
 

#using built in python function
#time complexity: O(n) where n is the input number
#space complexity: O(n) where n is the input number



class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
           res.append(i.bit_count())
        return res


#using bit manipulation
#time complexity: O(n) where n is the input number
#space complexity: O(n) where n is the input number
#they say space complexity is O(1) since the output is not counted, but fuck em.


# Following the same principle of the previous approach, we can also have a transition function by playing with the least significant bit.

# Let look at the relation between x and x′=x/2

# x=(1001011101)2​ =(605)10​
 

# x′=(100101110)2 =(302)10
# ​
 

# We can see that x′ is differ than x by one bit, because x′ 
# can be considered as the result of removing the least significant bit of x.

# Thus, we have the following transition function of pop count P(x):

# P(x)=P(x/2)+(xmod2)

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for x in range(1, n + 1):
            # x // 2 is x >> 1 and x % 2 is x & 1
            ans[x] = ans[x >> 1] + (x & 1) 
        return ans 