#Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
#You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
#Return the answer with the smaller index first.

# hash map solution
# time complexity: O(n)
# space complexity: O(n)
# loops through array, difference between target and current number is stored as key, index stored as value
# if next number is in hash, return the index of the current number and the index of the next number
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, num in enumerate(nums):
            if num in hash:
                return [hash[num], i]
            hash[target - num] = i