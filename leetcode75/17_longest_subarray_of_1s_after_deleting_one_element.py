

#two pointer solution
#time complexity O(n)
#space complexity O(1)

#similar to previous
#keep track of bool to show if the replacement has been used
#keep l at 0
#loop through r
#if nums[r] not a 1
#check if replacement used, if so, loop l until it reaches not a 1, increment it once after the not a 1
#set used to false to break loop, then to true inside of the if

#keep track of max count with max(maxCount, r-1) we dont do a +1 here since one is deleted

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxCount = 0
        used = False
        l = 0
        for r in range(len(nums)):
            if nums[r] != 1:
                if used:
                    while used:
                        if nums[l] != 1:
                            used = False
                        l += 1
                used = True
            maxCount = max(maxCount, r - l)
        return maxCount