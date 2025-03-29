# binary search solution
# time complexity O(log n)
# space complexity O(1)


# like the find min in rotated sorted array, but instead of returning the min, return the index of the target
# basically you want to find if you're in the left sorted or right sorted portion of array
# [4,5,6,7,0,1,2]
#  left     right

# you do this by checking if the mid point is greater than the left pointer

# if you're in the left portion
# check if the target is greater than the mid point, or less than the left pointer
# if so, you want shift to the right by moving the left pointer
# otherwise, shift left by moving the right pointer

# if you're in the right portion
# check if the target is less than the mid point, or greater than the right pointer
# if so, shift left by moving the right pointer
# otherwise, shift right by moving the left pointer
# return if the target is the midpoint
# return -1 if not found

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            #left sorted portion
            if nums[l] <= nums[m]:
                #target is greater than mid, shift right
                #target is less than left pointer, also shift right
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else: 
                    r = m - 1
            # right sorted array
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
