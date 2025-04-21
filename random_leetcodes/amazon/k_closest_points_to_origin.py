# You are given an 2-D array points where points[i] = [xi, yi] represents the coordinates of a point on an X-Y axis plane. 
# You are also given an integer k.
# Return the k closest points to the origin (0, 0).
# The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).
# You may return the answer in any order.

# Example 1:
# Input: points = [[0,2],[2,2]], k = 1
# Output: [[0,2]]
# Explanation : The distance between (0, 2) and the origin (0, 0) is 2. The distance between (2, 2) and the origin is sqrt(2^2 + 2^2) = 2.82842. So the closest point to the origin is (0, 2).

# Example 2:
# Input: points = [[0,2],[2,0],[2,2]], k = 2
# Output: [[0,2],[2,0]]
# Explanation: The output [2,0],[0,2] would also be accepted.


#optimal solution using priority queue with heap 

#time complexity O(k * logn)
#space complexity O(n)

# given the formula to determine the distance between points
#remember that ^2 operator doesn't work in python, use ** instead
#math.pow(x, y) also works
#the formula is
#(sqrt((x1 - x2)^2 + (y1 - y2)^2))
#since x2 and y2 are always 0, we can just the formula to (sqrt(x1^2 + y1^2))
#x^2 + y^2 also works since we just want whats bigger and not the exact value

#initialize a heap
#heapify the heap
#iterate through the points
#calculate the distance using the formula
#push the distance and the point to the heap, the distance is the priority
#when we pop, the lowest priority will pop first, which equates to the smallest distance

#iterate through the heap k times
#append the point to the result list
#return the result list



class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minH = []
        for x, y in points:
            distance = math.sqrt((x ** 2 + y ** 2))
            heapq.heappush(minH, (distance, [x, y]))
        res = []
        while len(res) < k:
            x, y = heapq.heappop(minH)[1]
            res.append([x, y])
        return res