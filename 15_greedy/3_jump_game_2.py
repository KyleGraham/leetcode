# You are given an array of integers nums, where nums[i] represents the maximum length of a jump towards the right from index i. 
# For example, if you are at nums[i], you can jump to any index i + j where:

# j <= nums[i]
# i + j < nums.length
# You are initially positioned at nums[0].

# Return the minimum number of jumps to reach the last position in the array (index nums.length - 1). You may assume there is always a valid answer.

# Example 1:
# Input: nums = [2,4,1,1,1,1]
# Output: 2
# Explanation: Jump from index 0 to index 1, then jump from index 1 to the last index.

# Example 2:
# Input: nums = [2,1,2,1,0]
# Output: 2

#solution using greedy
#time complexity: O(n)
#space complexity: O(1)

#initialize res as 0, this is the amount of jumps
#initialize l and r as 0, this is the left and right side of the window (r is the max jump of options, l is the current jump)
#while r is less than the last index of nums
#initialize farthest as 0, this is the farthest we can jump
#loop through the array from l to r + 1
#update farthest to the max of farthest and the current index plus the number at that index
#update l to r + 1, this is the next jump
#update r to farthest, this is the max jump of options
#increment res by 1, this is the amount of jumps
#return res at the end

class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0 #window

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, nums[i] + i)
            l = r + 1
            r = farthest
            res += 1
        return res