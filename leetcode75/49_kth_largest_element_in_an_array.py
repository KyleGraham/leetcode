# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

 

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4



#solution using max heap
#time complexity O(nlogk) each n elements processed once and heap operations take logk 
#space complexity O(k)

#just make a max heap by doing a negative min heap
#pop the elements in a loop in range k - 1
#then return the first element in the heap



class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)
        for i in range(k - 1):
            heapq.heappop(nums)
        return nums[0] * -1