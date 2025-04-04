# You are given an array of integers candidates, WHICH MAY CONTAIN DUPLICATES, and a target integer target. 
# Your task is to return a list of all unique combinations of candidates where the chosen numbers sum to target.

# Each element from candidates may be chosen at most once within a combination. The solution set must not contain duplicate combinations.

# You may return the combinations in any order and the order of the numbers in each combination can be in any order.

# Example 1:
# Input: candidates = [9,2,2,4,6,1,5], target = 8
# Output: [
#   [1,2,5],
#   [2,2,4],
#   [2,6]
# ]

# Example 2:
# Input: candidates = [1,2,3,4,5], target = 7
# Output: [
#   [1,2,4],
#   [2,5],
#   [3,4]
# ]

#backtracking solution
#time complexity: O(2^n)
#space complexity: O(n)

#difference here between combination_target_sum.py is that we are not given a unique list of candidates
#so we need to skip duplicates while checking if a duplicate is in a solution

#initialize the result list
#sort the candidates, this will ensure duplicates are next to each other

#initialize the dfs function with i, cur as the current list, and total
#check if total equals the target
#if so, append a copy of the current list to the result list and return
#check if i is out of bounds or if total is bigger than target
#if so, return

#append the current number to the current list
#recursive call the function with the current index +1, current list, and total + the current number
#pop the current number from the current list

#skip duplicates
#increment the index while the current number is the same as the next number and i+1 is less than the length of the candidates
#recursive call the function with the current index + 1, current list, and total

#call the dfs function with the index at 0, an empty list, and 0
#return the result list





class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            cur.pop()

            #skip duplicates
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res