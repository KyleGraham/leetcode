# Given an unsorted array of integers nums and an integer k, return the kth largest element in the array.
# By kth largest element, we mean the kth largest element in the sorted order, not the kth distinct element.
# Follow-up: Can you solve it without sorting?

# Example 1:
# Input: nums = [2,3,1,5,4], k = 2
# Output: 4

# Example 2:
# Input: nums = [2,3,1,1,5,5,4], k = 3
# Output: 4


#sub optimal solution using max heap
# time complexity: O(nlogk)
# space complexity: O(k)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #max heap, which is fun in python
        nums = [-num for num in nums]
        heapq.heapify(nums)
        for i in range(k - 1):
            heapq.heappop(nums)
        return heapq.heappop(nums) * -1
      
      
#optimal solution using quick select
#time complexity: O(n) on average, worst case O(n^2)
#space complexity: O(1)
#quick select is a variation of quick sort

#first assign k to the index of the kth largest element

#quick select function
#pivot is the last element
#set p as the leftmode node, since this is the variable of the index the pivot is compared to
#check if the current element is less than or equal to the pivot
#swap the current element with the element at index p
#increment p
#this will leave the elements less than or equal to the pivot to the left of p
#elements greater than the pivot will not move and will end up to the right of p

#swap the pivot with the element at index p
#if p is greater than k, recursively call the function on the left side
#if p is less than k, recursively call the function on the right side
#if p is equal to k, return the element



class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k #reassign to index in array we're lookin for

        def quickSelect(l, r):
            pivot = nums[r]
            p = l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = pivot, nums[p]
            if p > k:
                return quickSelect(l, p - 1)
            elif p < k:
                return quickSelect(p + 1, r)
            else: #p == k
                return nums[p]

        return quickSelect(0, len(nums) - 1)