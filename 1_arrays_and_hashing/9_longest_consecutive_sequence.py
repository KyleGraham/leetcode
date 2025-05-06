#leetcode solution. One below times out on leetcode. This essentially does the same thing

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)
        return longest_streak



# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. 
# The elements do not have to be consecutive in the original array.
# You must write an algorithm that runs in O(n) time.

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