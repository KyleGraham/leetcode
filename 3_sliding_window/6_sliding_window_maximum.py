# You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge of the array. 
# The window slides one position to the right until it reaches the right edge of the array.
# Return a list that contains the maximum element in the window at each step.


# brute force with better space complexity?
# does a sliding window finding the maximum in the window
# appends to result array if the length of the window is equal to k
# increments l, then checks if the maximum was just popped off by that
# if so, it resets r to l and calculates that window again
# if not, continues to the next value
# if negatives allowed, should initialize max to negative infinity - float('-inf')
# time complexity roughly O(nlogn)
# space complexity O(1)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = 0
        res = []
        max = -1
        while r < len(nums):
            if nums[r] > max:
                max = nums[r]
            if r - l + 1 == k:
                res.append(max)
                if max == nums[l]:
                    max = -1
                    l += 1
                    r = l
                else:
                    l += 1
                    r += 1
                
            else:
                r += 1
        return res
      
# deque solution using sliding window
# storing the indexes of the current value in the deque
# this removes the need to constantly check all values in the window for the maximum as the deque will only hold the maximum
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()  # index
        l = r = 0

        while r < len(nums):
            #remove any number smaller than the current number at position r from the deque
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            # remove the left value from the deque if it's out of bounds
            if l > q[0]:
                q.popleft()
            #check if the right pointer is not less than k before adding to output 
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output