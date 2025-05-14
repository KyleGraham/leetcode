
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1

#solution using slow/fast pointer
#time complexity: O(n)
#space complexity: O(1)

# [0,1,0,3,12]
#  L
#  R

# [0,1,0,3,12]
#  L R

# [1,0,0,3,12]
#  L R

# [1,0,0,3,12]
#    L R 

# [1,0,0,3,12]
#    L   R 

# [1,3,0,0,12]
#    L   R 

# [1,3,0,0,12]
#      L   R 

# [1,3,12,0,0]
#      L    R 

# [1,3,12,0,0]
#         L R 



class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1
        
        return nums 