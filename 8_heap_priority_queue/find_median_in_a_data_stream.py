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


#optimal solution using a min heap and max heap
# time complexity O(m*logn) for add num and O(1) for find median
# space complexity O(n)

#create 2 heaps, a max heap and a min heap
#max heap will store the lower n/2 numbers
#min heap will store the higher n/2 numbers

#remember max heaps be negative

#initialize the median to infinity
#initialize the pivot to 5 (arbitrary)

#heapify the 2 heaps

#addNum function
#check if the number is less than or equal to the pivot
#push the negative of the number to the max heap
#check if the number is greater than the pivot
#push the number to the min heap

#check if the length of the max heap and min heap is 1
#set the median to the number and return

#check if the difference between the length of the max heap and min heap is greater than 1
#check if the length of the max heap is greater than the length of the min heap
#pop the max heap and push the value to the min heap
#set the pivot to this popped value as well

#otherwise, pop the min heap and push the value to the max heap and set the pivot

#calculate the median
#check if the total length of the heaps is odd
#check if the length of the max heap is greater than the length of the min heap
#pop whichever heap has the greater length and set the median to the popped value
#push the popped value back to the heap

#if even, pop the max heap and min heap, add them together and divide by 2

#findMedian function
#return the median


class MedianFinder:
  
    def __init__(self):
        #store numbers based on a pivot
        #say 5. So numbers less than 5 will be put into a max heap
        #then numbers greater than 5 will be put into a min heap

        #then when values are both greater than 1, check if they're unbalanced
        #and adjust the pivot based on this
        self.low_max_heap = []
        self.high_min_heap = []
        self.pivot = 5
        self.median = float('infinity')
        heapq.heapify(self.low_max_heap)
        heapq.heapify(self.high_min_heap)
        

    def addNum(self, num: int) -> None:
        if num <= self.pivot:
            heapq.heappush(self.low_max_heap, num * -1)
        elif num > self.pivot:
            heapq.heappush(self.high_min_heap, num)
        l_len = len(self.low_max_heap)
        r_len = len(self.high_min_heap)
        if l_len + r_len == 1:
            self.median = num
            return

        if abs(l_len - r_len) > 1:
            #check if the difference between the lenghts of heaps is at least 2
            #then they are unbalanced
            #if odd total num, value will be 1
            #if even, value should be 0
            if l_len > r_len:
                val = heapq.heappop(self.low_max_heap) * -1
                self.pivot = val
                heapq.heappush(self.high_min_heap, val)
            else:
                val = heapq.heappop(self.high_min_heap)
                self.pivot = val
                heapq.heappush(self.low_max_heap, val * -1)
        #calculate median
        l_len = len(self.low_max_heap)
        r_len = len(self.high_min_heap)
        total_len = l_len + r_len
        if total_len % 2:
            #odd
            if l_len > r_len:
                self.median = heapq.heappop(self.low_max_heap) * -1
                heapq.heappush(self.low_max_heap, self.median * -1)
            else:
                self.median = heapq.heappop(self.high_min_heap)
                heapq.heappush(self.high_min_heap, self.median)
        else:
            l = heapq.heappop(self.low_max_heap) * -1
            r = heapq.heappop(self.high_min_heap)
            self.median = (l + r) / 2
            heapq.heappush(self.low_max_heap, l * -1)
            heapq.heappush(self.high_min_heap, r)

    def findMedian(self) -> float:
        return self.median
        
        