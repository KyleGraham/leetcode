# You are given two integer arrays forward and backward, both of size n. You are also given another integer array queries.

# There are n houses arranged in a circle. The houses are connected via roads in a special arrangement:

# For all 0 <= i <= n - 2, house i is connected to house i + 1 via a road with length forward[i] meters. 
# Additionally, house n - 1 is connected back to house 0 via a road with length forward[n - 1] meters, completing the circle.
# For all 1 <= i <= n - 1, house i is connected to house i - 1 via a road with length backward[i] meters. 
# Additionally, house 0 is connected back to house n - 1 via a road with length backward[0] meters, completing the circle.
# You can walk at a pace of one meter per second. Starting from house 0, find the minimum time taken to visit each house in the order specified by queries.

# Return the minimum total time taken to visit the houses.

 

# Example 1:

# Input: forward = [1,4,4], backward = [4,1,2], queries = [1,2,0,2]

# Output: 12

# Explanation:

# The path followed is 0(0) → 1(1) →​​​​​​​ 2(5) → 1(7) →​​​​​​​ 0(8) → 2(12).

# Note: The notation used is node(total time), → represents forward road, and → represents backward road.

# Example 2:

# Input: forward = [1,1,1,1], backward = [2,2,2,2], queries = [1,2,3,0]

# Output: 4

# Explanation:

# The path travelled is 0 →​​​​​​​ 1 →​​​​​​​ 2 →​​​​​​​ 3 → 0. Each step is in the forward direction and requires 1 second.

 

# Constraints:

# 2 <= n <= 105
# n == forward.length == backward.length
# 1 <= forward[i], backward[i] <= 105
# 1 <= queries.length <= 105
# 0 <= queries[i] < n
# queries[i] != queries[i + 1]
# queries[0] is not 0.


#solution using prefix sums
#time complexity O(n + q) where n = len(forward) and q = len(queries)
#space complexity O(n) for the 2 prefix sum arrays

# Build two prefix‐sum arrays of length n+1:

# fwd[i] = total forward distance from house 0 to house i,
# bwd[i] = total backward distance from house 0 to house i.
# Iterate through queries, keeping track of the current house cur. For each target q:

# Compute the clockwise distance cw using fwd wrapping around if needed.
# Compute the counter clockwise distance ccw using bwd.
# Add min(cw, ccw) to the answer and set cur = q.
# Return the accumulated total




class Solution:
    def minTotalTime(self, forward: List[int], backward: List[int], queries: List[int]) -> int:
        n = len(forward)
        fwd = [0] * (n + 1)
        bwd = [0] * (n + 1)
        for i in range(1, n + 1):
            fwd[i] = fwd[i-1] + forward[i-1]
            bwd[i] = bwd[i-1] + (backward[i] if i<n else backward[0])
        res = 0
        cur = 0

        for q in queries:
            #from
            f = cur
            #to
            t = q
            if f <= t: 
                cw = fwd[t] - fwd[f]
            else:
                cw = fwd[n] - (fwd[f] - fwd[t])
            
            if f >= t:
                ccw = bwd[f] - bwd[t]
            else:
                ccw = bwd[n] - (bwd[t] - bwd[f])
            res += min(cw, ccw)
            cur = t
        return res
