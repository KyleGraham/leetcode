

# You are given a 2-D integer array points, where points[i] = [xi, yi]. Each points[i] represents a distinct point on a 2-D plane.

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between the two points, i.e. |xi - xj| + |yi - yj|.

# Return the minimum cost to connect all points together, such that there exists exactly one path between each pair of points.

# Example 1:
# Input: points = [[0,0],[2,2],[3,3],[2,4],[4,2]]
# Output: 10


#use prims algorithmn because its a minimum spanning tree (MST) problem



#must create n-1 edges to connect n nodes
#start at any node
#perform a bfs on that node

#keep a visit hash set
#keep a frontier (min heap) of edges 
# (every possible node that can be added from that position) (weight of adding that node, node) so it can be sorted by min weight

#go to node
#bfs the node
#add the node to the visit set
#add all options to the frontier
#pop the min weight node from the frontier

#exit case is if the visit set is equal to the number of nodes


#optimum solution using prims algo with an adjacency list and min heap doing bfs
#time complexity: O(n^2logn) where n is the number of nodes
#space complexity: O(n^2) where n is the number of nodes

#start by initializing N as the number of points
#initialize the adjacency list as a dictionary with the point as the key and the neighbors as (value, weight) pairs
#loop through the points
#initialize x1, y1 as the coordinates of the first point
#loop through i+1 to N as j
#initialize x2, y2 as the coordinates of the second point
#calculate the distance as the manhattan distance between the two points (abs(x1 - x2) + abs(y1 - y2))
#add the distance to the adjacency list as a tuple of (distance, point)
#add the distance to the adjacency list of the second point as a tuple of (distance, point)

#prims
#initialize the result variable as 0
#initialize a visit set
#initialize the min heap with (0, 0) where 0 is the starting point and 0 is the initial cost
#while the length of the visit set is less than N
#pop the cost and point from the min heap
#check if the point is in the visit set
# if so, continue since we've already visited it
#increment the result by the cost
#add the point to the visit set
#loop through the neighbors of the point
#check if the neighbor is not in the visit set
# if so, add the neighbor to the min heap with the distance as the cost
#outside the loop, return the result


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i:[] for i in range(N)} # i : list of [cost, node]
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        #prims algo
        res = 0
        visit = set()
        minH = [[0, 0]] # [cost, point]
        while len(visit) < N:
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])
        return res