
# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k 
# and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

# Example 1:

# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
# Example 2:

# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.
# Example 3:

# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

#one pass solution
#uses the if, elif, else to determine 3 values in increasing order

#first_num, second_num filled in order. any new values have to be greater than either before hitting the else




class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_num = float('inf')
        second_num = float('inf')
        for n in nums:
            if n <= first_num:
                first_num = n
            elif n <= second_num:
                second_num = n
            else:
                return True
        return False