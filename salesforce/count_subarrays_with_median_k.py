# You are given an array nums of size n consisting of distinct integers from 1 to n and a positive integer k.

# Return the number of non-empty subarrays in nums that have a median equal to k.

# Note:

# The median of an array is the middle element after sorting the array in ascending order. If the array is of even length, the median is the left middle element.
# For example, the median of [2,3,1,4] is 2, and the median of [8,4,3,5,1] is 4.
# A subarray is a contiguous part of an array.
 

# Example 1:

# Input: nums = [3,2,1,4,5], k = 4
# Output: 3
# Explanation: The subarrays that have a median equal to 4 are: [4], [4,5] and [1,4,5].
# Example 2:

# Input: nums = [2,3,1], k = 3
# Output: 1
# Explanation: [3] is the only subarray that has a median equal to 3.

# Constraints:

# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i], k <= n
# The integers in nums are distinct.


#solution using prefix sum of the counts
#time complexity O(n)
#space complexity O(n)

# Use a HashMap/dict to count the frequencies of the prefix sum of the running balance (bigger ones - smaller ones);

# If k is the median of a subarray, it must present in the subarray. 
# Therefore, before finding the median, no subarray ending at current element meets the problem requirement;

# After finding kduring traversal, no need to count the frequencies any more in the HashMap/dict. 
# If number of bigger ones == number of the smaller (or + 1), that is, 
# the difference between prefix sum of balances (bigger - smaller) is 0 or 1, 
# then kis the median of the subarray ending at current element;

# Use the difference of prefix sums to get the count of the required number of subarrays.

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        prefix = Counter([0])
        balance = 0
        res = 0
        found = False
        
        for num in nums:
            if num < k:
                balance -= 1
            elif num > k:
                balance += 1
            else:
                found = True
            if found:
                res += prefix[balance] + prefix[balance - 1]
            else:
                prefix[balance] += 1
        return res