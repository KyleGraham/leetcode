# Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q, 
# return the lowest common ancestor (LCA) of the two nodes.
# The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q as descendants. 
# The ancestor is allowed to be a descendant of itself.

# Example 1:
# Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8
# Output: 5

# Example 2:
# Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 4
# Output: 3
# Explanation: The LCA of nodes 3 and 4 is 3, since a node can be a descendant of itself.

#optimal solution using iteration
#time complexity O(logn)
#space complexity O(1)

#important here that the nodes are unique values, and that the bst is sorted so we can use that to our advantage
#since a node can be an ancestor of itself if its val = p or q, then if this is the case, we return that node
#otherwise, we traverse the tree
#we check if both the p and q values are greater than the current node, then we traverse the right side of the tree
# we check if both the p and q values are less than the current node, then we traverse the left side of the tree
# if the above two conditions are not met, then we return the current node
# conditions here are that one value is greater than the current node and the other is less than the current node or that one equals the cur node

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
