# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
# write a function to check whether these edges make up a valid tree.

# Example 1:
# Input:
# n = 5
# edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
# Output:
# true

# Example 2:
# Input:
# n = 5
# edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
# Output:
# false
# Note:
# You can assume that no duplicate edges will appear in edges. 
# Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.



#solution using dfs and adjacency list
# # time complexity: O(V + E) where V is number of vertices and E is number of edges
# # space complexity: O(V + E) where V is number of vertices and E is number of edges

#fill our adjacency list preMap with edges for 0 to n-1 along with empty lists
# #loop through the edges
# #add the edge to the preMap
#since these are undirected edges, we add both directions

#initialize the cycle set.
#this will be used to detect cycles. It's also used to make sure all nodes are connected since all must be able to be reached by the dfs to 0

#call dfs on the first node, 0 with -1 as a default prev
#if it returns false, return false

#check that the length of the cycle set is equal to n
# if not, return false since not all nodes are connected
#otherwise, return true

#the dfs function
#takes in node and prev. Since we're taking in both edges, we have to make sure we don't go back to the previous node
#because it will be a false positive for a cycle if we do

#check if the node is in the cycle set
# if so, return false since we have a cycle
#add the node to the cycle set
#loop through the edges of the node from the adjacency list
#check if the previous node is not equal to the current node and if dfs returns false
# if so, return false since we have a cycle
#return true outside the loop




class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(n)}
        for edge in edges:
            preMap[edge[0]].append(edge[1])
            preMap[edge[1]].append(edge[0])
        cycle = set()

        def dfs(node, prev):
            if node in cycle:
                return False
            cycle.add(node)
            for pre in preMap[node]:
                if not pre == prev and not dfs(pre, node):
                    return False
            return True

        if not dfs(0, -1):
            return False
            
        if not n == len(cycle):
            return False
        return True