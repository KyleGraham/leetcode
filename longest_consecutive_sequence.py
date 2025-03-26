# optimal solution
# make the list a set so that it removes duplicates
# find the potential starts of any consecutive sequence by determining of the number before the current number is in the set
# loop through the potential starts and find the length of the consecutive sequence
# return the longest sequence
# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        starts = []
        topCount = 0
        for num in nums:
            if num - 1 not in numSet:
                starts.append(num)
        for start in starts:
            length = 1
            while (start + length in numSet):
                length += 1
            topCount = max(topCount, length)
        return topCount