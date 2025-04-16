
# You are given an array of non-overlapping intervals intervals where intervals[i] = [start_i, end_i] 
# represents the start and the end time of the ith interval. intervals is initially sorted in ascending order by start_i.

# You are given another interval newInterval = [start, end].

# Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i 
# and also intervals still does not have any overlapping intervals. You may merge the overlapping intervals if needed.

# Return intervals after adding newInterval.

# Note: Intervals are non-overlapping if they have no common point. For example, [1,2] and [3,4] are non-overlapping, but [1,2] and [2,3] are overlapping.

# Example 1:
# Input: intervals = [[1,3],[4,6]], newInterval = [2,5]
# Output: [[1,6]]

# Example 2:
# Input: intervals = [[1,2],[3,5],[9,10]], newInterval = [6,7]
# Output: [[1,2],[3,5],[6,7],[9,10]]


#greedy solution
#time complexity: O(n)
#space complexity: O(1) extra space, O(n) for the output

#initialize res as an empty list
#loop through the intervals
#check if the newInterval ends before the current interval starts
#this means the new interval is before the current interval
# if so, append the newInterval to res and return res plus the rest of the intervals

##check if the newInterval starts after the current interval ends
#this means the new interval is after the current interval
# if so, append the current interval to res

#else, this means theres overlap
#set newInterval to: [ min of the first elements in both intervals, max of the second elements in both intervals]
#we don't set it here just incase the new interval overlaps with the next interval

#at the end, append the newInterval to res
#and return res


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval [1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]), 
                    max(newInterval[1], intervals[i][1])
                ]
        res.append(newInterval)
        return res