#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
#The output should not contain any duplicate triplets. You may return the output and the triplets in any order.


#basically a for loop with two pointers to do binary search
# #time complexity: O(n^2)
# #space complexity: O(m) m = number of triplets and n is length of given array

#start by sorting the array so that we can binary search
#initialize a res array
#loop through the array, can use enumerate or just index
#check if the current number is greater than 0, 
# if so break since they're sorted and we wont get negatives on the right side of a 0

#check if it's not the first index and the previous number is the same as the current number
# if so, skip it, continue

#initialize two pointers, one at the left at i+1 and one at the right at len(nums) - 1
#while the left pointer is less than the right pointer
#sum the three numbers
#check if the sum is less than 0, if so move the left pointer to the right
#check if the sum is greater than 0, if so move the right pointer to the left
#check if the sum is equal to 0, if so append the triplet to the res array
#increment the left pointer and decrement the right pointer
#check if the next value of the left pointer is the same as the current value, if so skip it, l+=1

#return res


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            if a > 0:
                break
            #check not first position and prev value == cur
            if i > 0 and nums[i - 1] == a:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum = a + nums[l] + nums[r]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res

