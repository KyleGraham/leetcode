#You are given an array non-negative integers height which represent an elevation map. 
# Each value height[i] represents the height of a bar, which has a width of 1.
#Return the maximum area of water that can be trapped between the bars.

#Optimal solution using two pointers
# time complexity O(n)
# space complexity O(1)
# set two pointers at the start and end of the array
# set leftMax and rightMax to the height of the left and right pointers
# while the height at the left pointer is less than the height at the right pointer
#  increment left pointer check how much water can be stored at that point. Since Max is called, it can never be negative
# while height of right pointer is less or equal to left pointer, decrement right pointer and check how much water can be stored at that point
# return the total area
# areas are always positive, but need to check empty list edge case
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        area = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                area += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                area += rightMax - height[r]
        return area
