# You are given a connected undirected graph with n nodes labeled from 1 to n. Initially, it contained no cycles and consisted of n-1 edges.

# We have now added one additional edge to the graph. 
# The edge has two different vertices chosen from 1 to n, and was not an edge that previously existed in the graph.

# The graph is represented as an array edges of length n where edges[i] = [ai, bi] represents an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the graph is still a connected non-cyclical graph. 
# If there are multiple answers, return the edge that appears last in the input edges.

# Example 1:



# Input: edges = [[1,2],[1,3],[3,4],[2,4]]

# Output: [2,4]
# Example 2:



# Input: edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]

# Output: [3,4]

#soution using union find
#time complexity: O(v + (E * α(v))) where v is number of vertices and E is number of edges
#space complexity: O(v) where v is number of vertices
#α(v) is the inverse Ackermann function, which grows very slowly. So we can consider it as O(1) for practical purposes
#thats what amortized complexity is apparently

#similar to count_connected_components. 
#basically we create the parent array and rank array. Then if a node comes in that is already in the parent array, we know we have a cycle

#initialize N as len(edges)
#initialize parent array with each node as its own parent so [0, 1, 2, 3, 4] in range N + 1 since we have N edges
#initialize rank array with 1 for each node
#initialize find function
#takes in n
#if n is not equal to its parent (par[n] != n)
#call the find function recursively and set par[n] to the result of the find function
#return the parent of n

#initialize union function
#takes in n1 and n2
#find the parent of n1 and n2, (p1, p2 = find(n1), find(n2))
#check if the parents are equal
# # if so, return false since they are already in the same component
#check if the rank of p2 is greater than p1
# # # if so, set the parent of p1 to p2 and increment the rank of p2 by the rank of p1
# # #otherwise, set the parent of p2 to p1 and increment the rank of p1 by the rank of p2
# # #return true since we successfully unioned the two components

#loop through edges, with n1 and n2 being the nodes in the edges
#call the union function on n1,n2 and check if it returns false
#return n1,n2 if false since we have a cycle

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        par = [i for i in range(N + 1)]
        rank = [1] * (N + 1)

        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]
            
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]