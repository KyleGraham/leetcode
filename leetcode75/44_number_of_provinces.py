
# There are n cities. Some of them are connected, while some are not. 
# If city a is connected directly with city b, 
# and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, 
# and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

 

# Example 1:


# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
# Example 2:


# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3


#solution using dfs
#time complexity O(N^2) go through each node and each connected node
#space complexity O(N)

#the difficulty comes in the weird way the data is given to you
#[[1,1,0], [1,1,0], [0,0,1]]

# city |  which node city connects to
# --------
# 0     | (connects to city 0) , (connects to city 1), (not connect to city 2) 
# 1     | (connects to city 0) , (connects to city 1), (not connect to city 2) 
# 2     | (not connect to city 0), (not connect to city 1), (connects to city 2)

#its not an adjacency list or an actual matrix where the row/col is a node. its some weird shit

#basically looping through the rows
#checking if the row is not in visit
# if not, add to the result and dfs on it

#the dfs
#add the val to the visit set
#loop through N for the cols
#check if the row/col combo is 1 in isConnected and the col is not in visit
#if so, dfs on i

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        N = len(isConnected)
        visit = set()

        def dfs(cur):
            visit.add(cur)
            for i in range(N):
                if (isConnected[cur][i] == 1 and i not in visit):
                    dfs(i)
        
        for i in range(N):
            if i not in visit:
                res += 1
                dfs(i)
        return res