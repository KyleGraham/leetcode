# Given a binary tree root, return the level order traversal of it as a nested list, 
# where each sublist contains the values of nodes at a particular level in the tree, from left to right.

# Example 1:
# Input: root = [1,2,3,4,5,6,7]
# Output: [[1],[2,3],[4,5,6,7]]

# Example 2:
# Input: root = [1]
# Output: [[1]]

# Example 3:
# Input: root = []
# Output: []

#since we're doing a level order traversal, we do bredth first search
#we use a queue to store the nodes
#we start with the root node
#we keep track of the level size which will equal to the length of the queue after the left and right nodes of each node are added
#keep track of an array that stores the vales of the nodes at each level
#find the len of the queue levelSize
#loop through the levelSize, can do a forloop on len(levelSize) or a while loop on levelSize != 0 with a -= decrement
#pop the first node from the queue, remember to use popleft() since its a deque
#append the value of the node to the level array
#decrement the levelSize
#add the left and right nodes of the node to the queue if they exist

#outside of the while loop, append the level array to the res array
#return the res array

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return []
        queue = deque([root])
        while queue:
            levelSize = len(queue)
            level = []
            while levelSize != 0:
                node = queue.popleft()
                level.append(node.val)
                levelSize -= 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res