# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2


#dfs solution
#time complexity O(n)
#space complexity O(1)

#remember to use self.res for the val here
#rest is straight forward. just dfs and make res the max depth. Pass in depth to the dfs function


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root, depth):
            if not root:
                return
            self.res = max(depth, self.res)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        dfs(root, 1)
        return self.res