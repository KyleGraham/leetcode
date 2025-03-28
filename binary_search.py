#given an array of integers in sorted ascending order, return index of target value with binary search

#search array regular binary search
# time complexity: O(log n)
# space complexity: O(1)
# usual binary search setup
# check if the middle element is greater than or less than the target
# if greater, move the right pointer to the left
# if less, move the left pointer to the right
# remember to reduce right pointer by 1 and increase left pointer by 1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1