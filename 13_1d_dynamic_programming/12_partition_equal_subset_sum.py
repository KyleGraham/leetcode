
# You are given an array of positive integers nums.

# Return true if you can partition the array into two subsets, 
# subset1 and subset2 where sum(subset1) == sum(subset2). Otherwise, return false.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: true
# Explanation: The array can be partitioned as [1, 4] and [2, 3].

# Example 2:
# Input: nums = [1,2,3,4,5]
# Output: false


#solution using dynamic programming bottom up with hash set
#time complexity: O(n * t) where n is len of nums and t is target
#space complexity: O(t) where t is target

#check if the sum of the numbers is odd
#if so, impossible so return False

#initialize target as the sum of the numbers divided by 2
#initialize dp as a set with 0
#loop through the list from the end to the beginning
#initialize a temp set nextDP
#for each number in dp
#check if the current number plus the number is equal to target
#return True if so
#add the number to the current number in dp and add it to nextDP
#add the number to nextDP

#outside the dp for loop, set dp to nextDP
#outside the loop, 
#return true if target is in dp, else false



class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2
        dp = set()
        dp.add(0)

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                #little optimization to return earlier if its found
                if (t + nums[i]) == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return True if target in dp else False