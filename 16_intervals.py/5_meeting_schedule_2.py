
# Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] 
# (start_i < end_i), find the minimum number of days required to schedule all meetings without any conflicts.

# Example 1:
# Input: intervals = [(0,40),(5,10),(15,20)]
# Output: 2
# Explanation:
# day1: (0,40)
# day2: (5,10),(15,20)

# Example 2:
# Input: intervals = [(4,9)]
# Output: 1
# Note:

# (0,8),(8,10) is not considered a conflict at 8


#two pointer solution 
#time complexity O(NlogN) where N is the number of intervals
#space complexity O(N)

#start by sorting the intervals by start time for the start array
#and end time for the end array
#initialize res and count to 0
#initialize s and e to 0 for start and end
#while s is less than the length of intervals
#check if the start time of the current interval is less than the end time of the current interval
#this means we have a collision
#increment s by 1 and count by 1 because we have another meeting occurring
#otherwise, increment e by 1 and decrement count by 1 because a meeting ended
#update res to be the max of res and count
#return res at the end


"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res = count = 0
        s = e = 0 #start and end
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res