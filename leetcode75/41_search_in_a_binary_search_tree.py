# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

 

# Example 1:


# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]
# Example 2:


# Input: root = [4,2,7,1,3], val = 5
# Output: []



#solution using dfs
#time complexity O(h) h for height of tree
#space complexity O(h)

#just check if the val is greater than target, move right if so
#val less than target, move left
#val equal to target, return that node



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.res = None
        def dfs(root):
            if not root:
                return
            if val > root.val:
                dfs(root.right)
            elif val < root.val:
                dfs(root.left)
            else:
                self.res = root
        dfs(root)
        return self.res