# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


#sliding window solution
#time complexity O(n)
#space complexity O(1)

#loop through array with r while keeping l at 0
#keep track of number of zeroes encountered
#when num of zeroes == k, increment L until zeroes is no longer k
#keep track of max count with max(maxCount, r - l + 1)



class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        maxCount = 0
        zeroes = 0
        l = 0
        r = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                while zeroes == k:
                    if nums[l] == 0:
                        zeroes -= 1
                    l += 1
                zeroes += 1
            maxCount = max(maxCount, r - l + 1)
        return maxCount

