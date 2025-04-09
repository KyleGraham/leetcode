# You are given an integer array nums where nums[i] represents the amount of money the ith house has. 
# The houses are arranged in a circle, i.e. the first house and the last house are neighbors.

# You are planning to rob money from the houses, but you cannot rob two adjacent houses 
# because the security system will automatically alert the police if two adjacent houses were both broken into.

# Return the maximum amount of money you can rob without alerting the police.

# Example 1:
# Input: nums = [3,4,3]
# Output: 4
# Explanation: You cannot rob nums[0] + nums[2] = 6 because nums[0] and nums[2] are adjacent houses. The maximum you can rob is nums[1] = 4.

# Example 2:
# Input: nums = [2,9,8,3,6]
# Output: 15
# Explanation: You cannot rob nums[0] + nums[2] + nums[4] = 16 because nums[0] and nums[4] are adjacent houses. The maximum you can rob is nums[1] + nums[4] = 15.


#house robber 1 but the houses are in a circle so you can't rob the last house if you rob the first
#dyanmic programming using bottom up approach
#time complexity O(n)
#space complexity O(1)

#basically using the solution from house robber 1
#putting it in a helper function. Then calling it twice
#once with the first element removed and once with the last element removed
#then returning the max of both

#we check if len(nums) == 1 or 2
#because 1 element is removed, we hit that len(1) edge case if it starts at 2
#so if one, return the first element, if 2, return the max of both elements


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        def helper(nums):
            for i in range(len(nums) -3, -1, -1):
                if i + 3 >= len(nums):
                    nums[i] = nums[i] + nums[i + 2]
                else:
                    nums[i] = nums[i] + max(nums[i + 2], nums[i + 3])
            return max(nums[0], nums[1])

        return max(helper(nums[1:]), helper(nums[:-1]))