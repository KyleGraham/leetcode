# There is an undirected graph with n nodes. 
# There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

# The nodes are numbered from 0 to n - 1.

# Return the total number of connected components in that graph.

# Example 1:
# Input:
# n=3
# edges=[[0,1], [0,2]]
# Output:
# 1

# Example 2:
# Input:
# n=6
# edges=[[0,1], [1,2], [2,3], [4,5]]
# Output:
# 2

#solution using union find
#time complexity: O(v + (E * α(v))) where v is number of vertices and E is number of edges
#space complexity: O(v) where v is number of vertices
#α(v) is the inverse Ackermann function, which grows very slowly. So we can consider it as O(1) for practical purposes
#thats what amortized complexity is apparently

#essentially, we make a parent array and a rank array
#the parent array is used to find the parent of each node
#the rank array is used to keep track of the size of each component

#start by initializing parent array with each node as its own parent so [0, 1, 2, 3, 4]
#initialize rank array with 1 for each node

#result starts at n
#for every successful union, result is decremented by the 1. So on union function success, we return 1, otherwise we return 0
#so loop through edges, with n1 and n2 being the nodes in the edges
#call union on n1 and n2 (res -= union(n1, n2))
#decrement result by the return value of union
#return result at the end

#find function
#takes in n1
#initialize res to n1 since default is its a parent of itself
#while res is not equal to its parent (while res != par[res]:)
# #set the parent of res to its parent (par[res] = par[par[res]]) (this basically sets the parent to the grandparent if it has one)
# #set res to its parent (res = par[res])
#return res

#union function
#takes in n1 and n2
#find the parent of n1 and n2, (p1, p2 = find(n1), find(n2))
#check if the parents are equal
# # if so, return 0 since they are already in the same component
#check if the rank of p2 is greater than p1
# # if so, set the parent of p1 to p2 and increment the rank of p2 by the rank of p1
# #otherwise, set the parent of p2 to p1 and increment the rank of p1 by the rank of p2
# #return 1 since we successfully unioned the two components


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1
            
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res






#dfs solution using adjacency list
# # time complexity: O(V + E) where V is number of vertices and E is number of edges
# # space complexity: O(V + E) where V is number of vertices and E is number of edges

#solution using union find is better space complexity and I think better time complexity. It uses amortized complexity and I'm not sure how that compares
#for this problem, we're counting connected components. So how many nodes connected with other nodes seperately
#so [0, 1], [1, 2], [3, 4] would be 2 connected components, since 0, 1, 2 are connected and 3, 4 are connected
#essentially, we make an adjacency list and fill it from edges
#we initialize a visit set

#initialize a count of 0
#loop through the nodes
#check if the node is not in the visit set
# if so, call dfs on the node
#increment the count by 1
#return the count

#the dfs function
#takes in the node
#check if the node is in the visit set
# if so, return
#add the node to the visit set
#loop through the edges of the node from the adjacency list
#call dfs on the node
#return


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        preMap = {i:[] for i in range(n)}
        for edge in edges:
            preMap[edge[0]].append(edge[1])
            preMap[edge[1]].append(edge[0])
        visit = set()

        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for pre in preMap[node]:
                dfs(pre)
            return

        count = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                count += 1
                
        return count