#Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

#Hash set solution
#Time complexity: O(n)
#Space complexity: O(n)
class Solution:
  def hasDuplicate(self, nums: List[int]) -> bool:
    hash = {}
    hasDuplicate = False
    for num in nums:
        if num in hash:
            hasDuplicate = True
        hash[num] = num

    return hasDuplicate