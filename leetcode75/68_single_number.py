

#math solution
# time complexity: O(n)
# space complexity: O(1)

#basically 2∗(a+b+c)−(a+a+b+b+c)=c
#first part doubles every number, then we subtract the sum of all the numbers, which leaves us with the single number.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)
    


#bit manipulation solution
# time complexity: O(n)
# space complexity: O(1)

# Concept

# If we take XOR of zero and some bit, it will return that bit
# a⊕0=a
# If we take XOR of two same bits, it will return 0
# a⊕a=0
# a⊕b⊕a=(a⊕a)⊕b=0⊕b=b
# So we can XOR all bits together to find the unique number.

class Solution(object):
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a
    
