# You are given an array of integers stones where stones[i] represents the weight of the ith stone.
# We want to run a simulation on the stones as follows:
# At each step we choose the two heaviest stones, with weight x and y and smash them togethers
# If x == y, both stones are destroyed
# If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# Continue the simulation until there is no more than one stone remaining.
# Return the weight of the last remaining stone or return 0 if none remain.

# Example 1:
# Input: stones = [2,3,6,2,4]
# Output: 1
# Explanation:
# We smash 6 and 4 and are left with a 2, so the array becomes [2,3,2,2].
# We smash 3 and 2 and are left with a 1, so the array becomes [1,2,2].
# We smash 2 and 2, so the array becomes [1].

# Example 2:
# Input: stones = [1,2]
# Output: 1


#optimal solution using a max heap
#since map heap doesn't exist in python, this becomes more complicated
#initialize a new list with the negative values of the stones
#heapify the list
#while the length of the list is greater than 1
#pop the first two elements
#check if the second element is greater than the first, since in order the opposite can never be true, and if equal both destroyed anyways
#and they negative so the normal comparison is reversed
#push the difference of the two elements back into the list

#add a zero to the list to return the last element
#since other values are negative, this zero will be [1] if there is a value in the list
#return the absolute value of the zero index

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        newStones = []
        for s in stones:
            newStones.append(s * -1)
        #or stones = [-s for s in stones]
        heapq.heapify(newStones)
        while len(newStones) > 1:
            first = heapq.heappop(newStones)
            second = heapq.heappop(newStones)
            #should be second < first, but negatives to reverse
            #since in order, no need to check the opposite
            if second > first:
                heapq.heappush(newStones, first - second)

        #adds a zero to the heap as a default, if any value
        #exists in the heap already, this will not be the 0 index
        newStones.append(0)
        return abs(newStones[0])
      
      
      
      