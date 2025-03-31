# Given the root of a binary tree, return its depth.
# The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:
# Input: root = [1,2,3,null,null,4]
# Output: 3

# Example 2:
# Input: root = []
# Output: 0

# recursive depth first search solution
# time complexity O(n)
# space complexity O(n)

# set a max_depth variable to 0. State variable so it doesn't get reset

#call the dfs function with the root and 0 depth
#return the max_depth

#dfs function
#check if the root is empty
#increment the depth
#set max_depth to the max of max_depth and depth
#recursively call the function on the left and right
#return nothing

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 0
        self.dfs(root, 0)
        return self.max_depth

    def dfs(self, root, depth):
        if not root:
            return
        depth += 1
        self.max_depth = max(self.max_depth, depth)
        self.dfs(root.left, depth)
        self.dfs(root.right, depth)