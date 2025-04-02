#optimal solution using backtracking or like tree maze algorithm? 
#time complexity: O(2 * t/m) where t is the given target and m is the max value in nums
#space complexity: O(t/m) where t is the given target and m is the max value in nums

#initialize result list
#initialize the dfs function with i, cur as the current list, and total as the parameters

#check if the total is equal to the target
#append a copy of the current list to the result list

#check if the given i is out of bounds of the list nums, or if total is greater than the target
#if so, return

#append the current number to the current list
#recursive call the function with the current index, current list, and total + the current number

#pop the current number from the current list
#recursive call the function with the current index incremented by 1, current list, and total

#call the dfs function with the index at 0, an empty list, and 0
#return the result list

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            #decision 1, include the current num
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            cur.pop()
            dfs(i + 1, cur, total)
        dfs(0, [], 0)
        return res








#less optimal brute force solution
#because we have to check if the subset is in the result array, adds extra computation vs ensuring no duplicates exist

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        subset = []
        def dfs(i):
            total = sum(subset)
            if i >= len(nums):
                return
            if (total >= target):
                if total == target:
                    if not subset in res:
                        res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            dfs(i)
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res