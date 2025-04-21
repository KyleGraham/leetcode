# The median is the middle value in a sorted list of integers. 
# For lists of even length, there is no middle value, so the median is the mean of the two middle values.

# For example:

# For arr = [1,2,3], the median is 2.
# For arr = [1,2], the median is (1 + 2) / 2 = 1.5
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far.

# Example 1:

# Input:
# ["MedianFinder", "addNum", "1", "findMedian", "addNum", "3" "findMedian", "addNum", "2", "findMedian"]

# Output:
# [null, null, 1.0, null, 2.0, null, 2.0]

# Explanation:
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.findMedian(); // return 1.0
# medianFinder.addNum(3);    // arr = [1, 3]
# medianFinder.findMedian(); // return 2.0
# medianFinder.addNum(2);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0

#new shorter leetcode solution
# time complexity O(m*logn) for add num and O(1) for find median
# space complexity O(n)

#initialize the min and max heap, small and large. Small is the max heap, large is the min heap
#small is negative because max heap is not built in python


#addNum
#check if the length of the small and large heaps are equal
#if so, heappush to self.large the negative value of heappushpop self.small the negative of num
#basically:
# The new number is first added to the max-heap (self.small).
# Then, the largest element from the max-heap is moved to the min-heap (self.large).
# This ensures that self.large will have one more element than self.small.

# When len(self.small) != len(self.large) (which means self.large has one more element):

# The new number is first added to the min-heap (self.large).
# Then, the smallest element from the min-heap is moved to the max-heap (self.small).
# This equalizes the heaps so they have the same number of elements.


#find median
#check if the length of the small and large heaps are equal
#if so, return the average of the first element in the large heap and the negative of the first element in the small heap divided by 2
#otherwise, return the first element in the large heap
#the large heap will always have the larger number, so we return that

from heapq import *


class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            #push to self.small negative num, then pop from self.small and push to self.large
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            #push to self.large, then pop from self.large and push to self.small
            #this ensures that self.large will always have one more element than self.small unless they equal
            
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])

        
        