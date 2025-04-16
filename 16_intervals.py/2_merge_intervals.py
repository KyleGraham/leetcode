
# Given an array of intervals where intervals[i] = [start_i, end_i], 
# merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# You may return the answer in any order.

# Note: Intervals are non-overlapping if they have no common point. 
# For example, [1, 2] and [3, 4] are non-overlapping, but [1, 2] and [2, 3] are overlapping.

# Example 1:
# Input: intervals = [[1,3],[1,5],[6,7]]
# Output: [[1,5],[6,7]]

# Example 2:
# Input: intervals = [[1,2],[2,3]]
# Output: [[1,3]]

#solution using sorting
##time complexity: O(n log n)
##space complexity: O(n), O(1) or O(n) depending on the sorting algo, O(n) for the output

#start by sorting the intervals on the start value
#initialize output with the first interval
#loop through the intervals starting at index 1
#check if the start value of the current interval is less than or equal to the end value of the last interval in output
#this means we can merge the intervals
#update the end value of the last interval in output to be the max of the end values of both intervals, we use lastMin since sorted
#otherwise, we can't merge the intervals
#append the current interval to output

#return output




class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1] #get end value of most recent interval put in output

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end) #since sorted, this start is the min
                                                  #just need the max of the last vals
            else:
                output.append([start, end])
        return output