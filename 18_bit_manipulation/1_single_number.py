# You are given a non-empty array of integers nums. Every integer appears twice except for one.

# Return the integer that appears only once.

# You must implement a solution with 

# O(n) runtime complexity and use only 

# O(1) extra space.

# Example 1:
# Input: nums = [3,2,3]
# Output: 2

# Example 2:
# Input: nums = [7,6,6,7,8]
# Output: 8

#solution using the exclusive or operator ^
#time complexity: O(n)
#space complexity: O(1)

#because we have duplicates of all numbers except 1, the ^ operator will cancel out the duplicates
#and return the unique number


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = num ^ res
        return res