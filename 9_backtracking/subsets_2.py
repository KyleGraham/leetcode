# You are given an array nums of integers, WHICH MAY CONTAIN DUPLICATES. Return all possible subsets.
# The solution must not contain duplicate subsets. You may return the solution in any order.

# Example 1:
# Input: nums = [1,2,1]
# Output: [[],[1],[1,2],[1,1],[1,2,1],[2]]

# Example 2:
# Input: nums = [7,7]
# Output: [[],[7], [7,7]]


#this is basically subsets but with duplicates
#can handle it the way combination_target_sum_2.py handles duplicates basically

#solution using backtracking
#time complexity: O(n * 2^n)
#space complexity: O(2^n) for output list, O(n) extra space

#sort the list
#initialize the result list
#initialize the subset list

#dfs function taking in the current index
#check if the index is greater than or equal to the length of the list
#append a copy of the subset to the result list and return

#add the num at the current index to the subset
#recursive call the function with the index incremented by 1
#pop the num from the subset

#skip duplicates
#while the next index is not out of bounds and the current num is the same as the next num
#increment the index

#recursive call the function with the index incremented by 1

#call the dfs function with the index at 0
#return the result list

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1)
        dfs(0)
        return res