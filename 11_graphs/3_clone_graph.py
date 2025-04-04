

# dfs solution
#time complexity: O(V + E) where V is number of vertices and E is number of edges
#space complexity: O(V) where V is number of vertices

#use hash map to keep track of our nodes and which ones are already created
#call dfs with the passed in node

#dfs function
#check if the node is in the hash map
# if so, return the node
#copy the node
#add the node to the hash map
#loop through the neighbors of the node
#call dfs on each neighbor and append it to the copy node
#return the copy node


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        oldToNew = {}

        #essetially copying the node, then copying the neighbors recursively
        def dfs(n):
            if n in oldToNew:
                return oldToNew[n]
            copy = Node(n.val)
            oldToNew[n] = copy
            for neighbor in n.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        return dfs(node)




# bfs
#time complexity: O(V + E) where V is number of vertices and E is number of edges
#space complexity: O(V) where V is number of vertices

#use hash map to keep track of our nodes and which ones are already created
#then use it to create the neighbors

# check for null node, return None if so
#initialize the hash map
#add current node to the hash map
#initialize a deque with the current node added
#while the deque is not empty
#pop the left item from the deque
#for loop on all neighbors from popped item
#check if the neighbor is not in the hash map
# if so, add it to the hash map and the deque
#append the hash map item of the neighbor to the hash map item of the current node

#return the hash map item of the passed in node outside the while loop


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        oldToNew = {}
        oldToNew[node] = Node(node.val)
        q = deque([node])
        while q:
            cur = q.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in oldToNew:
                    oldToNew[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                oldToNew[cur].neighbors.append(oldToNew[neighbor])
        return oldToNew[node]
        
