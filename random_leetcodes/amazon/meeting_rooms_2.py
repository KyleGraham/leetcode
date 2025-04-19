# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], 
# return the minimum number of conference rooms required.

# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2
# Example 2:

# Input: intervals = [[7,10],[2,4]]
# Output: 1

#leet code problem is a bit different
#instead of having the intervals be objects with start and end, they're just arrays
#so we use sorted to sort the start and end times (start = sorted(i[0] for i in intervals)
#and end = sorted(i[1] for i in intervals))

#rest of the solution is the same
#initialize res and count to 0
#initialize s and e to 0, these are the start and end pointers

#while s is less than the length of the intervals
#check if the start time is less than the end time
#increment the count and s, since theres a meeting
#otherwise decrement the count and increment e, since the meeting is over
#update res to be the max of res and count outside of the if else
#return res



class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted(i[0] for i in intervals)
        end = sorted(i[1] for i in intervals)
        res = count = 0
        s = e = 0
        while s < len(intervals):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(res, count)
        return res