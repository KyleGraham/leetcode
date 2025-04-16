# Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] 
# (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts.

# Example 1:

# Input: intervals = [(0,30),(5,10),(15,20)]

# Output: false
# Explanation:

# (0,30) and (5,10) will conflict
# (0,30) and (15,20) will conflict
# Example 2:

# Input: intervals = [(5,8),(9,15)]

# Output: true
# Note:

# (0,8),(8,10) is not considered a conflict at 8


#solution using sorting
#time complexity: O(n log n)
#space complexity: O(n), O(1) or O(n) depending on the sorting algo

#start by sorting the intervals on the start value
#initialize prevEnd to the end value of the first interval
#loop through the intervals starting at index 1
#check if the start value of the current interval is less than or equal to prevEnd
#this means we have an overlap
#return False
#otherwise, update prevEnd to the end value of the current interval
#return True at the end


"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        if len(intervals) == 0:
            return True
        prevEnd = intervals[0].end
        for i in range(1, len(intervals)):
            if prevEnd > intervals[i].start:
                return False
            prevEnd = intervals[i].end
        return True