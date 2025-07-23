# You are given an array of integers cost where cost[i] is the cost of taking a step from the ith floor of a staircase. 
# After paying the cost, you can step to either the (i + 1)th floor or the (i + 2)th floor.

# You may choose to start at the index 0 or the index 1 floor.

# Return the minimum cost to reach the top of the staircase, i.e. just past the last index in cost.

# Example 1:
# Input: cost = [1,2,3]
# Output: 2
# Explanation: We can start at index = 1 and pay the cost of cost[1] = 2 and take two steps to reach the top. The total cost is 2.

# Example 2:
# Input: cost = [1,2,1,2,1,1,1]
# Output: 4
# Explanation: Start at index = 0.


#dynamic programming solution bottom up
#time complexity O(n)
#space complexity O(n)

#start at the end of the array and work backwards
#for each index, we set the value to the cost of the current index and the min of jumping 1 or 2
#then we return the min of the two possible starting indexes


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cost.append(0)

        #we do -3 because it ignores the 0 index in the 
        #last position we added, the second to last since it
        #will never change, and the -1 always added
        for i in range(len(cost) - 3, -1, -1):
            #set cost[i] to the min value of jumping 1 or 2
            #could also do
            #cost[i] += min(cost[i + 1], cost[i + 2]) since cost[i] duplicated
            cost[i] = min(cost[i] + cost[i + 1], cost[i] + cost[i + 2])
        #return min of both possible start indexes
        return min(cost[0], cost[1])
