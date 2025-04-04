# You are given an integer array heights where heights[i] represents the height of the ithbar.
#You may choose any two bars to form a container. Return the maximum amount of water a container can store.

# optimal solution using two pointers
# time complexity O(n)
# space complexity O(1)
# usual two pointer setup
# calculate area based on distance between right and left pointer, and the minimun height
# instead of incrementing both pointers, only increment the one that's the smaller height
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            area = (r - l) * min(heights[r], heights[l])
            if area > maxArea:
                maxArea = area
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return maxArea