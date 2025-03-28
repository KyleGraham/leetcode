# You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.
# Return the area of the largest rectangle that can be formed among the bars.
# Note: This chart is known as a histogram.
# Example 1:
# Input: heights = [7,1,7,2,2,4]
# Output: 8
# Example 2:
# Input: heights = [1,3,7]
# Output: 7



#solution using stack
# time complexity O(n)
# space complexity O(n)
# initialize maxArea to 0
# initialize stack, this will hold an array of the height and index
# iterate through the heights
# set start to the current index
# while loop that checks if the stack is not empty and the last height in the stack is greater than the current height
# pop the stack, calculates the potential area and set maxArea to the max of the two
# set start to the index of the popped height
# append the current height and index to the stack

# after the loop, iterate through the stack and calculate the area of the remaining heights


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # (index and height)
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
         