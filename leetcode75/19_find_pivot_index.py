
#solutiong using "prefix sum" idea
#time complexity O(n)
#space complexity O(1)

#sum all the nums
#keep track of leftsum
#loop through nums with enumerate
#check if the leftsum is equal to the total sum - left sum - the cur val
#if so, return the index since the sum of the left is the same as the sum of the right
#add the cur val to leftsum
#return -1 outside of loop if val not found

class Solution(object):
    def pivotIndex(self, nums):
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1



#solution using prefix suffix, but not needed worse space complexity of O(n)
#leetcode keeps labeling these as prefix questions and not using prefix


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i+1] + nums[i + 1]
        
        for i in range(n):
            if suffix[i] == prefix[i]:
                return i
        return -1