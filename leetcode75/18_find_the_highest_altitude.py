

#don't actually need a prefix sum for this, just the idea?
#time complexity O(n)
#space complexity O(1)

#just initialize cur as 0, keep track of res
#loop through gain
#add the val to cur, then set res to max of res and cur

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur = 0
        res = cur
        
        for alt in gain:
            cur += alt
            res = max(res, cur)
        
        return res


#solution using prefix sum. This has a space complexity of O(n) which is worse than solution above. Don't need the whole array


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix = [0] * (len(gain) + 1)
        for i in range(len(gain)):
            prefix[i] = prefix[i - 1] + gain[i]
        return max(prefix)