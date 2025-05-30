# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.



# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

# Two binary trees are considered leaf-similar if their leaf value sequence is the same.

# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

# Example 1:


# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Output: true
# Example 2:


# Input: root1 = [1,2,3], root2 = [1,3,2]
# Output: false

#solution using dfs
#time complexity O(n)
#space complexity O(n)

#basically just getting the leaf nodes for 2 trees and comparing
#pass in the arrays into the dfs function to fill them
#then compare equality


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        vals1 = []
        vals2 = []

        def dfs(root, res):
            if not root:
                return
            if not root.left and not root.right:
                res.append(root.val)
            dfs(root.left, res)
            dfs(root.right, res)
            
        dfs(root1, vals1)
        dfs(root2, vals2)
        return vals1 == vals2