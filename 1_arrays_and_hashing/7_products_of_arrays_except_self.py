#Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
#Each product is guaranteed to fit in a 32-bit integer.
#Follow-up: Could you solve it in O(n) time without using the division operation?


# brute force
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        returnArr = [0] * len(nums)
        for i in range(len(nums)):
            sum = 1
            for j in range(len(nums)):
                if j != i:
                    sum *= nums[j]
            returnArr[i] = sum
        return returnArr
#optimal using prefix and suffix
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      n = len(nums)
      res = [0] * n
      pref = [0] * n
      suff = [0] * n
      #make the first val of prefix and last val of suffix 1
      pref[0] = suff[n - 1] = 1
      for i in range(1, n):
          #generate prefix array by multiplying the previous value with the current value
          pref[i] = nums[i - 1] * pref[i - 1]
      for i in range(n - 2, -1, -1):
          #generate suffix array by multiplying the next value with the current value
          suff[i] = nums[i + 1] * suff[i + 1]
      for i in range(n):
          #multiply the prefix and suffix array to get the product except self
          res[i] = pref[i] * suff[i] 
      return res