# You are given a network of n directed nodes, labeled from 1 to n.
# You are also given times, a list of directed edges where times[i] = (ui, vi, ti).

# ui is the source node (an integer from 1 to n)
# vi is the target node (an integer from 1 to n)
# ti is the time it takes for a signal to travel from the source to the target node (an integer greater than or equal to 0).
# You are also given an integer k, representing the node that we will send a signal from.

# Return the minimum time it takes for all of the n nodes to receive the signal. 
# If it is impossible for all the nodes to receive the signal, return -1 instead.

# Example 1:
# Input: times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]], n = 4, k = 1
# Output: 3

# Example 2:
# Input: times = [[1,2,1],[2,3,1]], n = 3, k = 2
# Output: -1

#solution using an adjacency list and dijkstra's algorithm
#time complexity: O(ElogV) where E is number of edges and V is number of vertices
#space complexity: O(V + E) where V is number of vertices and E is number of edges

#first step is to make the adjacency list
#it will store the nodes as the key, then the neighbors as (value, weight) pairs
#initialize the minHeap with (0, k) where k is the starting node, and the initial weight of 0 as it takes 0 time to get to the starting node
#initialize a visit set to keep track of the nodes we've already visited
#initialize a time variable to keep track of the total time it takes. This is the return val

#while the minHeap is not empty, pop the first element
#check if the current node is in the visit set
# if so, continue since we've already visited it
#add the current node to the visit set
#update the time variable to be the max of the current time and the distance
#loop through the neighbors of the current node
#check if the neighbor is not in the visit set
# if so, add the neighbor to the minHeap with the distance + the weight of the edge

#outside the loop, check if the length of the visit set is equal to n, if so return the t var, else return -1

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        minHeap = [(0, k)]
        visit = set()
        t = 0
        while minHeap:
            distance, current = heapq.heappop(minHeap)
            if current in visit:
                continue
            visit.add(current)
            t = max(t, distance)
            for neighbor, neighborDistance in edges[current]:
                if neighbor not in visit:
                    heapq.heappush(minHeap, (neighborDistance + distance, neighbor))
        return t if len(visit) == n else -1
