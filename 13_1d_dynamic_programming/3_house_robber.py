# You are given an integer array nums where nums[i] represents the amount of money the ith house has. 
# The houses are arranged in a straight line, i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.

# You are planning to rob money from the houses, but you cannot rob two adjacent houses 
# because the security system will automatically alert the police if two adjacent houses were both broken into.

# Return the maximum amount of money you can rob without alerting the police.

# Example 1:
# Input: nums = [1,1,3,3]
# Output: 4
# Explanation: nums[0] + nums[2] = 1 + 3 = 4.

# Example 2:
# Input: nums = [2,9,8,3,6]
# Output: 16
# Explanation: nums[0] + nums[2] + nums[4] = 2 + 8 + 6 = 16.

#dynamic programming solution using bottom up approach
#time complexity O(n)
#space complexity O(1)

#starging from the back of the array (we ignore the last two values since they dont change
#check if the index + 3 is greater than the length of the array (will be 3rd value from the back)
# if so, set the value to the cost of the current index and the cost of the index + 2
# if not, set the value to the cost of the current index and the max of the next two indices
#return the max of the first two values in the array, unless the len of the array is 1, then return the first value

class Solution:
    def rob(self, nums: List[int]) -> int:
        for i in range(len(nums) -3, -1, -1):
            if i + 3 >= len(nums):
                nums[i] = nums[i] + nums[i + 2]
            else:
                nums[i] = nums[i] + max(nums[i + 2], nums[i + 3])

        return max(nums[0], nums[1]) if len(nums) > 1 else nums[0]