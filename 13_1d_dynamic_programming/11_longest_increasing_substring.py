# Given an integer array nums, return the length of the longest strictly increasing subsequence.

# A subsequence is a sequence that can be derived from the given sequence by deleting some 
# or no elements without changing the relative order of the remaining characters.

# For example, "cat" is a subsequence of "crabt".
# Example 1:
# Input: nums = [9,1,4,2,3,3,7]
# Output: 4
# Explanation: The longest increasing subsequence is [1,2,3,7], which has a length of 4.

# Example 2:
# Input: nums = [0,3,1,3,2,3]
# Output: 4

#slightly better, but same idea essentially
#dynamic programming solution using bottom up
#time complexity: O(n^2)
#space complexity: O(n)

#initialize n as the len of nums
#initialize dp as a list of 1s with len(nums)
#loop through the list from the end to the beginning
#for each index, loop through the rest of the list
#check if the current index is less than the next index
#and if so, set dp[i] to the max of dp[i] and dp[j] + 1
#return the max value in dp

#Idea is to fill up the cache dp back to front with the max substring at each index
#then when we go to the next index, we check if it's value is less than the cur value
#and set the dp index to be the max of the two
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)




#my brute force approach using bottom up dynamic programming and a cache
#just slightly slower, probably from doing a while loop instead of a for loop for the j
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n:
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                j += 1
        return max(dp)