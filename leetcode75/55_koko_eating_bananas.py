# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
# The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas 
# and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead 
# and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

 

# Example 1:

# Input: piles = [3,6,7,11], h = 8
# Output: 4
# Example 2:

# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# Example 3:

# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
 

# Constraints:

# 1 <= piles.length <= 104
# piles.length <= h <= 109
# 1 <= piles[i] <= 109



#solution using binary search
#m = max number of bananas in a single pile
#time complexity: O(n * logm)
#space complexity: O(1)

#classic binary search but with r as max piles
#have to do math.ceil on the pile/m for time as there's no partials, pile has to be completed

#other weird stuff:
#wile l < r, since we return r
#            if t <= h:
            #     r = m
            # else:
            #     l = m + 1

#when setting right, don't do a -1, since we're returning right

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:  
        l = 1
        r = max(piles)
        while l < r:
            m = (l + r) // 2
            t = 0
            for pile in piles:
                t += math.ceil(pile / m)
            if t <= h:
                r = m
            else:
                l = m + 1
        return r
        