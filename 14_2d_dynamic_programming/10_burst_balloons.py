# You are given an array of integers nums of size n. 
# The ith element represents a balloon with an integer value of nums[i]. 
# You must burst all of the balloons.

# If you burst the ith balloon, you will receive nums[i - 1] * nums[i] * nums[i + 1] coins. 
# If i - 1 or i + 1 goes out of bounds of the array, then assume the out of bounds value is 1.

# Return the maximum number of coins you can receive by bursting all of the balloons.

# Example 1:

# Input: nums = [4,2,3,7]

# Output: 167

# Explanation:
# nums = [4,2,3,7] --> [4,3,7] --> [4,7] --> [7] --> []
# coins =  4*2*3    +   4*3*7   +  1*4*7  + 1*7*1 = 143

#solution using dynamic programming top down with memoization
#time complexity: O(n^3)
#space complexity: O(n^2)

#essentially we're going to have choose a value to be the last balloon to burst
#then caculate the sub arrays of the left and right of it

#start by adding a 1 to the left and right of the nums array nums = [1] + nums + [1]
#initialize a dp cache as a hashmap 

#initialize a dfs function that takes in l and r as the left and right indexes
#check if l is greater than r, if so return 0
#check if the key is in the cache, if so return the value
#initialize the cache value to 0
#loop through the array from l to r + 1
#calculate the coins by multiplying the left and right values of l and r with the current index
#add the dfs of the left and right indexes to the coins
#update the cache value to the max of the current cache value and coins
#return the cache value

#finally, return the dfs of 1 and len(nums) - 2 since we added 1s to the left and right of the array

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}
        
        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            dp[(l, r)] = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1] 
                coins += dfs(l, i - 1)
                coins += dfs(i + 1, r)
                dp[(l, r)] = max(dp[(l, r)], coins)
            return dp[(l, r)]

        return dfs(1, len(nums) - 2) #ignore the 1s added on l and r