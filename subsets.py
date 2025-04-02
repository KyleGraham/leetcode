# Given an array nums of unique integers, return all possible subsets of nums.

# The solution set must not contain duplicate subsets. You may return the solution in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:
# Input: nums = [7]
# Output: [[],[7]]


#optimal solution using backtracking
#time complexity: O(n * 2^n)
#space complexity: O(n) extra space, O(2^n) subsets

#essentially is going to be a decision tree where you can either include or not include a current number

#so for [1,2,3]
#branch to [1] and []
#then for 2
#branch to [1,2], [1], [2], []
#then for 3
#branch to [1,2,3], [1,2], [1,3], [1], [2,3], [2], [3], []

#initialize the result list
#initialize the subset list
#both are state functions technically since the dfs is initialized in the function

#dfs function
#check if the index is greater than or equal to the length of the list
#append the a copy of the subset to the result list so it wont be modified by the next recursive call accessing it

#decision to include the current number
#append the number to the subset
#recursive call the function with the index incremented by 1

#decision not to include the current number
#pop the number from the subset
#recursive call the function with the index incremented by 1

#call dfs with the index at 0
#return the result list



class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            #decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            #decision not to include nums[i]
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res