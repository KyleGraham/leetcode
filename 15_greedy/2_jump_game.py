
# You are given an integer array nums where each element nums[i] indicates your maximum jump length at that position.

# Return true if you can reach the last index starting from index 0, or false otherwise.

# Example 1:

# Input: nums = [1,2,0,1,0]

# Output: true
# Explanation: First jump from index 0 to 1, then from index 1 to 3, and lastly from index 3 to 4.

# Example 2:

# Input: nums = [1,2,1,0,1]

# Output: false

#solution using greedy
##time complexity: O(n)
##space complexity: O(1)

#initialize goal as the last index in nums
#loop through the array in reverse order
#check if the current index plus the number at that index is greater than or equal to goal
#this means we can reach the goal from this index
#update goal to the current index
#return true if goal is 0, else false

#essentially, we work from back to front, moving the goal post if we can reach it from the cur index


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0