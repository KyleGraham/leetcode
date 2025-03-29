# You are given an array of length n which was originally sorted in ascending order. 
# It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:
# [3,4,5,6,1,2] if it was rotated 4 times.
# [1,2,3,4,5,6] if it was rotated 6 times.
# Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array.
# Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.
# A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

# Example 1:
# Input: nums = [3,4,5,6,1,2]
# Output: 1

# Example 2:
# Input: nums = [4,5,0,1,2,3]
# Output: 0

# Example 3:
# Input: nums = [4,5,6,7]
# Output: 4

# binary search solution
# time complexity: O(log n)
# space complexity: O(1)
# usual binary search setup
# initialize res as the first element in array just incase it's been shifted to be actually sorted
#do while loop
# if the left pointer is less than or equal to the right pointer, value has basically already been found, so check with min on left pointer
# find the middle point
# if the middle point is greater than  the left pointer, you want to shift right because it's to the left of the pivot
# otherwise we want to shift it left as the pivot is on the left side
# return the result
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[0]
        while l <= r:
            if nums[l] < nums[r]: 
                res = min(res, nums[l])
                break
            
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res