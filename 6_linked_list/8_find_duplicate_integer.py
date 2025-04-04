# You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.
# Every integer appears exactly once, except for one integer which appears two or more times. Return the integer that appears more than once.

# Example 1:
# Input: nums = [1,2,3,2,2]
# Output: 2

# Example 2:
# Input: nums = [1,2,3,4,4]
# Output: 4

#Important thing here, the array contains n + 1 integers, and each integer is in the range [1, n] inclusive
#so we can use the values as indexes and traverse the array that way, making this a linked list cycle problem
#kind of a tortoise and hare problem, but using floyd's algorithm, the guy who made the problem and made the algorithm to solve it
#dick move honestly, even the guy making the explanation videos on youtube doesn't like it

# time complexity: O(n)
# space complexity: O(1)

#initialize slow and fast to 0, then move the pointers to the index of the value. Only twice with fast
# when they finally meet, create a second slow pointer
# loop through again, moving both slow pointers
# when they meet, return the value

#basically the fast pointer will loop through the cycle twice, and meet the slow pointer.
# then the second slow pointer starting from 0 will meet the first slow pointer at the duplicate value

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        return slow
        