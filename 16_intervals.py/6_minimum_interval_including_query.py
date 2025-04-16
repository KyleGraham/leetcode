# You are given a 2D integer array intervals, where intervals[i] = [left_i, right_i] 
# represents the ith interval starting at left_i and ending at right_i (inclusive).

# You are also given an integer array of query points queries. 
# The result of query[j] is the length of the shortest interval i such that left_i <= queries[j] <= right_i. 
# If no such interval exists, the result of this query is -1.

# Return an array output where output[j] is the result of query[j].

# Note: The length of an interval is calculated as right_i - left_i + 1.

# Example 1:
# Input: intervals = [[1,3],[2,3],[3,7],[6,6]], queries = [2,3,1,7,6,8]
# Output: [2,2,3,5,1,-1]
# Explanation:
# Query = 2: The interval [2,3] is the smallest one containing 2, it's length is 2.
# Query = 3: The interval [2,3] is the smallest one containing 3, it's length is 2.
# Query = 1: The interval [1,3] is the smallest one containing 1, it's length is 3.
# Query = 7: The interval [3,7] is the smallest one containing 7, it's length is 5.
# Query = 6: The interval [6,6] is the smallest one containing 6, it's length is 1.
# Query = 8: There is no interval containing 8.



#solution using min heap
#time complexity: O(n log n + m log m) where n is len of intervals and m is len of queries
#space complexity: O(n + m) where n is len of intervals and m is len of queries

#essentially, for every query, we add the intervals to a min heap (length, right)

#then we pop any min heap entries that have a right value less than the query
#then we set the result to the min heap entry with the smallest length
#since we sorted the queries, we use the dictionary values to create an array


#sort intervals
#initialize min heap
#initialize res as a dict
#initialize i as 0
#loop through the sorted queries with a while loop
#loop through i < len(intervals) and intervals[i][0] <= q #basically until we hit intervals with a start value greater than the query or run out of intervals
#push the length of the interval and the right value to the heap
#increment i

#while min heap and min heap[0][1] < q:
#pop the min heap

#res[q] = minHeap[0][0] if minHeap else -1 #make sure to check that the value exists, if not, -1
#initialize resArr as a list
#for q in queries:
#append res[q] to resArr
#return resArr




class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minHeap = []
        res = {} #start at dict, turn into array, so we can keep order of queries
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1
            
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1
        resArr = []
        for q in queries:
            resArr.append(res[q])
        return resArr





#brute force solution using hash
##time complexity: O(n * m) where n is len of intervals and m is len of queries
##space complexity: O(n) where n is len of intervals


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        hash = {}
        for l, r in intervals:
            c = r + 1 - l
            for i in range(l, r + 1):
                hash[i] = min(c, hash.get(i, float('infinity')))
        res = []
        for q in queries:
            res.append(hash.get(q, -1))
        return res