# Design a class to find the kth largest integer in a stream of values, including duplicates. 
# E.g. the 2nd largest from [1, 2, 3, 3] is 3. The stream is not necessarily sorted.

# Implement the following methods:
# constructor(int k, int[] nums) Initializes the object given an integer k and the stream of integers nums.
# int add(int val) Adds the integer val to the stream and returns the kth largest integer in the stream.

# Example 1:
# Input:
# ["KthLargest", [3, [1, 2, 3, 3]], "add", [3], "add", [5], "add", [6], "add", [7], "add", [8]]
# Output:
# [null, 3, 3, 3, 5, 6]
# Explanation:
# KthLargest kthLargest = new KthLargest(3, [1, 2, 3, 3]);
# kthLargest.add(3);   // return 3
# kthLargest.add(5);   // return 3
# kthLargest.add(6);   // return 3
# kthLargest.add(7);   // return 5
# kthLargest.add(8);   // return 6

#optimal solution using min heap
#time complexity O(nlogk)
#space complexity O(k)

#min heap is used to store the k largest elements
#initialize the min heap with the first k elements
#heapify the min heap
#check if the min heap is bigger than k elements when initialized
#pop the smallest element until the min heap has k elements

#add function
#check if the min heap has k elements
#use heapq.heappushpop to push the element and pop the smallest element to keep the heap at k elements
#otherwise, use heapq.heappush to add the element

#can also just do seperately, push the element, check if it has more than k, then pop if so

#return the smallest element in the min heap, which is the kth largest element

import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        self.k = k
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)


    def add(self, val: int) -> int:
        if len(self.min_heap) >= self.k:
            heapq.heappushpop(self.min_heap, val)
        else:
            heapq.heappush(self.min_heap, val)
        return self.min_heap[0]
            
