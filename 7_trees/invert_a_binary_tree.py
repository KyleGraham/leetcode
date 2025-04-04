# You are given the root of a binary tree root. Invert the binary tree and return its root.

# Example 1:
# Input: root = [1,2,3,4,5,6,7]
# Output: [1,3,2,7,6,5,4]

#optimal solution using recursive depth first search
#time complexity O(n)
#space complexity O(n)

#check for empty root, return null
#store either left or right in a temp value
#swap the left and the right
#set whatever one was wiped out as temp

#recursively call the function on the left and right order doesn't matter
#return the root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        #swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root