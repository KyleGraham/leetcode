
# Given an array nums of unique integers, return all the possible permutations. You may return the answer in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Example 2:
# Input: nums = [7]
# Output: [[7]]

#recursive solution
#time complexity: O(n! * n^2)
#space complexity: O(n! * n) for the output list

#idea here is to take the first number, then permute the rest of the numbers nums[1:] basically the list without the cur number

#then for each permutation, insert the current number at each index
#append the new permutation to the result list
#return the result list

#how this looks
# [1,2,3] -> [2,3] -> [3] -> []
# [] will go to 3, which will create [3]. Then it will go to 2 which will create [2,3] and [3,2] since 2 is added to start and end
#then wit will go to 1, which will create [1,2,3], [2,1,3], [2,3,1]  from [2,3]
# and [1,3,2], [3,1,2], [3,2,1] from [3,2]


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        perms = self.permute(nums[1:])
        res = []
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        return res