# Given an array of intervals intervals where intervals[i] = [start_i, end_i], 
# return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

# Note: Intervals are non-overlapping even if they have a common point. 
# For example, [1, 3] and [2, 4] are overlapping, but [1, 2] and [2, 3] are non-overlapping.

# Example 1:
# Input: intervals = [[1,2],[2,4],[1,4]]
# Output: 1
# Explanation: After [1,4] is removed, the rest of the intervals are non-overlapping.

# Example 2:
# Input: intervals = [[1,2],[2,4]]
# Output: 0

#greedy sort by end solution

#time complexity: O(n log n)
#space complexity: O(1) or O(n) depending on the sorting algo

#start by sorting the intervals on the end value
#initialize prevEnd to the end value of the first interval
#initialize res to 0
#loop through the intervals starting at index 1
#check if the start value of the current interval is less than or equal to prevEnd
#this means we have an overlap
#increment res by 1
#otherwise, update prevEnd to the end value of the current interval
#return res at the end


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        prevEnd = intervals[0][1]
        res = 0
        for i in range(1, len(intervals)):
            if prevEnd > intervals[i][0]:
                res += 1
            else:
                prevEnd = intervals[i][1]
        return res