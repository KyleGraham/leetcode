# Given a root node reference of a BST and a key, delete the node with the given key in the BST. 
# Return the root node reference (possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:

# Search for a node to remove.
# If the node is found, delete the node.
 

# Example 1:


# Input: root = [5,3,6,2,4,null,7], key = 3
# Output: [5,4,6,2,null,null,7]
# Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
# One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
# Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

# Example 2:

# Input: root = [5,3,6,2,4,null,7], key = 0
# Output: [5,3,6,2,4,null,7]
# Explanation: The tree does not contain a node with value = 0.
# Example 3:

# Input: root = [], key = 0
# Output: []


#solution using recursion
#time complexity O(logN)
#space complexity O(H)

#if node is a leaf, straightforward delete, node = null

# if Node is not a leaf and has a right child. Then the node could be replaced by its
# successor which is somewhere lower in the right subtree. Then one could proceed down recursively to delete the successor.

# Node is not a leaf, has no right child, and has a left child. 
# That means that its successor is somewhere upper in the tree but we don't want to go back. Let's use the predecessor 
# here which is somewhere lower in the left subtree. 
# The node could be replaced by its predecessor and then one could proceed down recursively to delete the predecessor.

# If key > root.val then delete the node to delete is in the right subtree root.right = deleteNode(root.right, key).

# If key < root.val then delete the node to delete is in the left subtree root.left = deleteNode(root.left, key).

# If key == root.val then the node to delete is right here. Let's do it :

# If the node is a leaf, the delete process is straightforward: root = null.

# If the node is not a leaf and has the right child, then replace the node value with a successor 
#     value root.val = successor.val, and then recursively delete, the successor in the right subtree root.right = deleteNode(root.right, root.val).

# If the node is not a leaf and has only the left child, then replace the node value with a predecessor 
#     value root.val = predecessor.val, 
#     and then recursively delete the predecessor in the left subtree root.left = deleteNode(root.left, root.val).

# Return root.

#Hope I dont see this in an interview


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def predecessor(self, root):
            root = root.left
            while root.right:
                root = root.right
            return root.val
    def successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not (root.left or root.right):
                root = None
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
        return root