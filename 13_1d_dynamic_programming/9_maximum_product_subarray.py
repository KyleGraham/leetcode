# Given an integer array nums, find a subarray that has the largest product within the array and return it.

# A subarray is a contiguous non-empty sequence of elements within an array.

# You can assume the output will fit into a 32-bit integer.

# Example 1:
# Input: nums = [1,2,-3,4]
# Output: 4

# Example 2:
# Input: nums = [-2,-1]
# Output: 2

#solution using prefix/suffix (basically just curMin/curMax)
#time complexity O(n)
#space complexity O(1)

#initialize res to the max of the nums
#this handles the single negative val edge case
#initialize curMin and curMax to 1, so if they are default and multiplied, the val says the same

#iterate through the nums
#set a temp for the current max since it will be overridden
#set the cur max as the max of all options (n * curMax, n * curMin, n)
# set the cur min as the min of all options (temp * n, n * curMin, n)
#set res to the max of res and curMax

#return res


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums) #possible single negative val
        curMin, curMax = 1,1

        for n in nums:
            temp = curMax
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(temp * n, n * curMin, n)
            res = max(res, curMax)
        return res