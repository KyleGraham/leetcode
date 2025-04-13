# You are given an array of integers nums and an integer target.

# For each number in the array, you can choose to either add or subtract it to a total sum.

# For example, if nums = [1, 2], one possible sum would be "+1-2=-1".
# If nums=[1,1], there are two different ways to sum the input numbers to get a sum of 0: "+1-1" and "-1+1".

# Return the number of different ways that you can build the expression such that the total sum equals target.

# Example 1:

# Input: nums = [2,2,2], target = 2

# Output: 3
# Explanation: There are 3 different ways to sum the input numbers to get a sum of 2.
# +2 +2 -2 = 2
# +2 -2 +2 = 2
# -2 +2 +2 = 2



#space optimized solution using dp and bottom up
#time complexity: O(n * m) where n is len of nums and m is the sum of all elementsin the array
#space complexity: O(m)

#initialize dp as a defaultdict of int
#essentially we keep track of a counter for each sum and store it in the defaultdict dp
#every num, we get the items in the default dict, then add a count for the current total + the num and - the num

#then we set the dp to the next dp
#we return the dp[target] at the end

#with the space optimization, we only keep track of the current row and the previous row because thats all we need
#normal solution just has multiple default dicts for every row basically 
#dp = [defaultdict(int) for _ in range(n + 1)]
#dp[0][0] = 1


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        for num in nums:
            next_dp = defaultdict(int)
            for total, count in dp.items():
                next_dp[total + num] += count
                next_dp[total - num] += count
            dp = next_dp
        return dp[target]
      
      
#normal solution
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(n):
            for total, count in dp[i].items():
                dp[i + 1][total + nums[i]] += count
                dp[i + 1][total - nums[i]] += count

        return dp[n][target]