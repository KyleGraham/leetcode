# two pointer optimal solution
# time complexity: O(n^2)
# space complexity: O(m) m = number of triplets and n is length of given array
#start by sorting the numbers so we can do binary search with the two pointers
#loop through the array, if the current number is the same as the previous number, skip it
#set two pointers, one at the beginning and one at the end
#while the left pointer is less than the right pointer, sum the three numbers
#if the sum is greater than 0, move the right pointer to the left
#if the sum is less than 0, move the left pointer to the right
#checr that the next value of the left pointer is not the same as the current value, if so skip
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solutions = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) -1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                elif sum == 0:
                    solutions.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return solutions