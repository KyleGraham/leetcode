# You are given an integer array nums and an integer k.

# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

# Return the maximum number of operations you can perform on the array.

 

# Example 1:

# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.
# Example 2:

# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.



#two pointer solution using sorting for binary search
#time complexity O(nlogn) due to sort
#space complexity: O(1)

#sort the nums, then use two pointer binary search based on the sum of the values in comparison to k
#if val greater than k, decrement r
#if val less than k, increment l


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        l = 0
        r = len(nums) - 1
        res = 0
        nums.sort()
        while l < r:
            val = nums[l] + nums[r]
            if val == k:
                res += 1
                l += 1
                r -= 1
            elif val > k:
                r -= 1
            else:
                l += 1
        return res