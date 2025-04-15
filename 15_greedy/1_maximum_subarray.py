# Given an array of integers nums, find the subarray with the largest sum and return the sum.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:
# Input: nums = [2,-3,4,-2,2,1,-1,4]
# Output: 8
# Explanation: The subarray [4,-2,2,1,-1,4] has the largest sum 8.

# Example 2:
# Input: nums = [-1]
# Output: -1


#solution using kadane's algorithm
#time complexity: O(n)
#space complexity: O(1)

#initialize maxSub as the first element in nums
#initialize curSum as 0
#for each number in nums
#check if curSum is less than 0, if so set it to 0, this ignores negatives
#add the number to curSum
#check if curSum is greater than maxSub, if so set maxSub to curSum
#return maxSub at the end


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub