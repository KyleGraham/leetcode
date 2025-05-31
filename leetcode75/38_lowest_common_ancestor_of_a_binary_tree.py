# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the
# lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

# Example 1:


# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# Example 2:


# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
# Example 3:

# Input: root = [1,2], p = 1, q = 2
# Output: 1


#solution using dfs
#time complexity O(n)
#space complexity O(h) for height of tree

#p and q are given as treenodes and the return is a treenode 

#basicaly, if root is either p or q, its going to be the LCA and you can return it
#on recursive calls, this also fills the left/right variables if one is found

#then call dfs on the left and right returning to the left and right variables respectively
#return the root if both left and right are found
#else return left or right as a bool if either are found

#outside return the dfs on root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if not root or root == p or root == q:
                return root
            left = dfs(root.left)
            right = dfs(root.right)
            if left and right:
                return root
            return left or right
        
        return dfs(root)