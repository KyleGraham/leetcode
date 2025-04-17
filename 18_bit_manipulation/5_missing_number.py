
#bitwise solution
#time complexity: O(n)
#space complexity: O(1)

#if you do the exclusive or for all the numbers from 0 to n and all the numbers in the array
#the result will be the missing number
#because the duplicates will cancel out
#and the missing number will be left


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xorr = n  
        for i in range(n):
            xorr ^= i ^ nums[i]
        return xorr
      

#math solution
#basiucally sum of n numbers - sum of the array
#the result will be the missing number
#time complexity: O(n)
#space complexity: O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]
        return res


#brute force using hash, not O(1) space
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numset = set(nums)
        n = len(nums)
        for i in range(n + 1):
            if i not in numset:
                return i
        
        
        
