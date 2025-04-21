# You are given an array of integers nums, there is a sliding window of size k which is moving from the 
# very left of the array to the very right. You can only see the k numbers in the window. 
# Each time the sliding window moves right by one position.

# Return the max sliding window.

 

# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]


#time complexity: O(n)
#space complexity: O(k) since the deque will only be size k

#uses a deque to keep track of the current max value in the window
#the deque will store the indices of the max values
#the first element of the deque will always be the max value in the window
#when the current index is greater than k, remove the first element of the deque
#remove all elements from the deque that are less than or equal to the current element
#append the current index to the deque
#check if the first value of the deque is outside the window, if so remove it
#check if i is greater than or equal to k - 1, if so append the first value of the deque to the result





class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() #stores indices
        res = []
        for i, cur in enumerate(nums):
            while q and nums[q[-1]] <= cur:
                q.pop()
            q.append(i)
            # remove first element if it's outside the window
            if q[0] == i - k:
                q.popleft()
            # if window has k elements add to results (first k-1 windows have < k elements
            #because we start from empty window and add 1 element each iteration)
            if i >= k - 1:
                res.append(nums[q[0]])
        return res