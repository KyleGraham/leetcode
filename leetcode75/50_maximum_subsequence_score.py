# You are given two 0-indexed integer arrays nums1 and nums2 of equal length n and a positive integer k. You must choose a subsequence of indices from nums1 of length k.

# For chosen indices i0, i1, ..., ik - 1, your score is defined as:

# The sum of the selected elements from nums1 multiplied with the minimum of the selected elements from nums2.
# It can defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]).
# Return the maximum possible score.

# A subsequence of indices of an array is a set that can be derived from the set {0, 1, ..., n-1} by deleting some or no elements.

 

# Example 1:

# Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
# Output: 12
# Explanation: 
# The four possible subsequence scores are:
# - We choose the indices 0, 1, and 2 with score = (1+3+3) * min(2,1,3) = 7.
# - We choose the indices 0, 1, and 3 with score = (1+3+2) * min(2,1,4) = 6. 
# - We choose the indices 0, 2, and 3 with score = (1+3+2) * min(2,3,4) = 12. 
# - We choose the indices 1, 2, and 3 with score = (3+3+2) * min(1,3,4) = 8.
# Therefore, we return the max score, which is 12.
# Example 2:

# Input: nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1
# Output: 30
# Explanation: 
# Choosing index 2 is optimal: nums1[2] * nums2[2] = 3 * 10 = 30 is the maximum possible score.
 

# Constraints:

# n == nums1.length == nums2.length
# 1 <= n <= 105
# 0 <= nums1[i], nums2[j] <= 105
# 1 <= k <= n


#solution using priority queue
#time complexity n(log n)
#space complexity O(n)

# Algorithm
# Store every pair (nums1[i], nums2[i]) in array pairs, and sort pairs by the second element (nums2[i]) in decreasing order.

# Use a min-heap top_k_heap to store the first k nums1[i] and a variable top_k_sum to store their sum.

# Initialize answer as the sum of elements in top_k_heap (i.e. top_k_sum) times pairs[k - 1][1].

# Iterate over indices starting from k, at each index i:

# Remove the smallest element stored in top_k_heap and from top_k_sum.
# Add the current nums1[i] to the heap and top_k_sum.
# Get the current score as the sum of top_k_heap (i.e. top_k_sum) times nums2[i], and update answer as the maximum score we have met.
# Return answer.


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(a, b) for a, b in zip(nums1, nums2)]
        pairs.sort(key = lambda x: -x[1])

        k_heap = [x[0] for x in pairs[:k]]
        k_sum = sum(k_heap)
        heapq.heapify(k_heap)

        res = k_sum * pairs[k - 1][1]

        for i in range(k, len(nums1)):
            k_sum -= heapq.heappop(k_heap)
            k_sum += pairs[i][0]
            heapq.heappush(k_heap, pairs[i][0])

            res = max(res, k_sum * pairs[i][1])

        return res