# Given the root of a binary tree, the value of a target node target, and an integer k, 
# return an array of the values of all nodes that have a distance k from the target node.

# You can return the answer in any order.

 

# Example 1:


# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
# Output: [7,4,1]
# Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
# Example 2:

# Input: root = [1], target = 1, k = 3
# Output: []


#bfs on generated graph
#time complexity O(n)
#space complexity O(n)

#basically generate an undirected graph from the binary tree
#and then do a bfs on the graph, adding to answer if distance is k

#initialize a graph as a defaultdict of lists
#build the graph using a recursive function
#the function takes the current node and its parent as arguments
#if cur and parent are not null, adds the parent to the graph of cur and cur to the graph of parent
#then it checks if the left and right children of cur are not null
#and calls the function recursively on the left and right children

#the graph building function is called on the root and None as the parent
#answer is initialized as an empty list
#visited is initialized as a set with the target value
#the target node is added to the queue with a distance of 0

#while the queue is not empty
#pop the current node and distance from the queue
#if the distance is equal to k, add the current node to the answer list
#continue to the next node
#otherwise, loop through the neighbors of the current node
#check if the neighbor is not in the visited set
# if so, add the neighbor to the visited set and append it to the queue with distance + 1
#return the answer list





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = collections.defaultdict(list)

        def build_graph(cur, parent):
            if cur and parent:
                graph[cur.val].append(parent.val)
                graph[parent.val].append(cur.val)
            if cur.left:
                build_graph(cur.left, cur)
            if cur.right:
                build_graph(cur.right, cur)
        
        build_graph(root, None)

        answer = []
        visited = set([target.val])

        #add the target node to the queue with a distance of 0
        queue = deque([(target.val, 0)])

        while queue:
            cur, distance = queue.popleft()
            #if the current node is at distance k from target,
            #add it to the answer list and continue to the next node.
            if distance == k:
                answer.append(cur)
                continue
            #add all unvisited neighbors of the current node to the queue
            for neighbor in graph[cur]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))
        return answer
