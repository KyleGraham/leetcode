
# You are given a 0-indexed integer array nums, where nums[i] is a digit between 0 and 9 (inclusive).

# The triangular sum of nums is the value of the only element present in nums after the following process terminates:

# Let nums comprise of n elements. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums of length n - 1.
# For each index i, where 0 <= i < n - 1, assign the value of newNums[i] as (nums[i] + nums[i+1]) % 10, where % denotes modulo operator.
# Replace the array nums with newNums.
# Repeat the entire process starting from step 1.
# Return the triangular sum of nums.

 

# Example 1:


# Input: nums = [1,2,3,4,5]
# Output: 8
# Explanation:
# The above diagram depicts the process from which we obtain the triangular sum of the array.
# Example 2:

# Input: nums = [5]
# Output: 5
# Explanation:
# Since there is only one element in nums, the triangular sum is the value of that element itself.



#in place solution using array
#time complexity: O(n^2) where n is len of nums
#space complexity: O(1)

#basically we loop through the array and add the current number to the next number then mod by 10 incase it goes over 10
#then we pop the last number off the array

#while the length of the array is greater than 1
#we loop through the array len - 1
#set the nums[i] to the current number plus the next number mod 10
#then we pop the last number off the array
#finally we return the first number in the array




class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            for i in range(len(nums) - 1):
                nums[i] = (nums[i] + nums[i + 1]) % 10
            nums.pop()
        return nums[0]