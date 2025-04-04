# You are given an integer array piles where piles[i] is the number of bananas in the ith pile. 
# You are also given an integer h, which represents the number of hours you have to eat all the bananas.
# You may decide your bananas-per-hour eating rate of k. 
# Each hour, you may choose a pile of bananas and eats k bananas from that pile. 
# If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.
# Return the minimum integer k such that you can eat all the bananas within h hours.

# Example 1:
# Input: piles = [1,4,3,2], h = 9
# Output: 2
# Explanation: With an eating rate of 2, you can eat the bananas in 6 hours.
# With an eating rate of 1, you would need 10 hours to eat all the bananas (which exceeds h=9), thus the minimum eating rate is 2.
# Example 2:
# Input: piles = [25,10,23,4], h = 4
# Output: 25

#binary search solution
# time complexity O(n log m) n = number of piles, m = max number of bananas in a pile
# space complexity O(1)

#doing the binary search on the eating speed, k since you want the least speed possible
#initialize left and right pointers, do the left at 1 since you can't eat 0 bananas
#right is the max of the number of bananas in a pile
#initialize res to the max number of bananas in a pile
#find mid point
#calculate eating time by looping through piles, then using math.ceil to round up since you can't eat partial bananas
# if the eating time is less than the total hours
# set res to k and move the right pointer to k - 1 to see if we can get it lower
# else move the left pointer to k + 1 to increase the eating speed
# return res

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #initialize k as half way point of hours for funzies
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            k = (r + l) // 2
            t = 0 #banana eating time
            #check how long to eat bananas
            for p in piles:
                t += math.ceil(p / k) 
            if t <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
        

