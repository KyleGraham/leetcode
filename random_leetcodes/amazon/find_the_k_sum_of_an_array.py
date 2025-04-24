# You are given an integer array nums and a positive integer k. You can choose any subsequence of the array and sum all of its elements together.

# We define the K-Sum of the array as the kth largest subsequence sum that can be obtained (not necessarily distinct).

# Return the K-Sum of the array.

# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

# Note that the empty subsequence is considered to have a sum of 0.

 

# Example 1:

# Input: nums = [2,4,-2], k = 5
# Output: 2
# Explanation: All the possible subsequence sums that we can obtain are the following sorted in decreasing order:
# - 6, 4, 4, 2, 2, 0, 0, -2.
# The 5-Sum of the array is 2.
# Example 2:

# Input: nums = [1,-2,3,4,-10,12], k = 16
# Output: 10
# Explanation: The 16-Sum of the array is 10.

# Time Complexity: O(NlogN + klogk) for sorting and heap operations
# Space Complexity: O(N + k), for using absNums, ans and maxHeap


# Key Strategy
# The solution uses a "build-down" approach, starting with the maximum possible sum and finding progressively smaller sums using a max heap.
# Step-by-Step Explanation:
# 1. Find the Maximum Possible Sum
# pythonmaxSum = sum([max(0, num) for num in nums])

# The maximum sum will include all positive numbers (or zeros) and exclude all negative numbers.
# This is the largest possible subsequence sum.

# 2. Prepare Absolute Values List
# pythonabsNums = sorted([abs(num) for num in nums])

# Convert all numbers to their absolute values and sort them.
# This helps us systematically explore smaller sums by considering whether to include/exclude each number.

# 3. Initialize a Max Heap
# pythonmaxHeap = [(-maxSum + absNums[0], 0)]

# Start with the maximum sum minus the smallest absolute value (which is at index 0 after sorting).
# We use a negative value because Python's heapq is a min-heap, but we need a max-heap.
# The tuple contains (modified sum, index in absNums).

# 4. Find the kth Largest Sum
# pythonans = maxSum
# count = 1
# while count < k:
#     nextSum, i = heapq.heappop(maxHeap)
#     ans = -nextSum
#     count += 1
#     if i + 1 < len(absNums):
#         heapq.heappush(maxHeap, (nextSum - absNums[i] + absNums[i + 1], i + 1))
#         heapq.heappush(maxHeap, (nextSum + absNums[i + 1], i + 1))

# Initially, ans is set to the maximum sum (1st largest sum)
# For each iteration, we pop the largest value from the heap to get the next largest sum
# We then generate two new possible sums by:

# Replacing the current absolute value with the next larger one
# Adding the next absolute value to our sum calculation



# 5. Return the kth Sum
# pythonreturn ans

# After finding the k-th largest sum, return it as the answer.

# Intuition Behind the Solution
# Imagine we're exploring a tree of possibilities:

# The root is the maximum sum (all positive numbers)
# At each level, we make decisions about whether to include or exclude elements
# By using a heap, we always explore the most promising (largest) sums first
# This ensures we find the k-th largest sum without having to calculate all 2^n possible subsequence sums

class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        maxSum = sum([max(0, num) for num in nums])
        absNums = sorted([abs(num) for num in nums])
        maxHeap = [(-maxSum + absNums[0], 0)]
        ans = maxSum
        count = 1
        while count < k:
            nextSum, i = heapq.heappop(maxHeap)
            ans = -nextSum
            count += 1
            if i + 1 < len(absNums):
                heapq.heappush(maxHeap, (nextSum - absNums[i] + absNums[i + 1], i + 1))
                heapq.heappush(maxHeap, (nextSum + absNums[i + 1], i + 1))
        return ans