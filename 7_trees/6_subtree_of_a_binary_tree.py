# Given the roots of two binary trees root and subRoot, 
# return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. 
# The tree tree could also be considered as a subtree of itself.

# Example 1:
# Input: root = [1,2,3,4,5], subRoot = [2,4,5]
# Output: true

# Example 2:
# Input: root = [1,2,3,4,5,null,null,6], subRoot = [2,4,5]
# Output: false

#solution using recursive depth first search
#time complexity O(n)
#space complexity O(n)

#check if subroot is empty, return True since any tree will have a node thats null
#check if root is empty, return False since a null tree can't have a subtree unless the subtree is null which we already checked

#check if the trees are the same
#return True if so

#recursively call the function on the left and right to check every node. Keep subRoot the same no .left or .right 
#the recursive calls return based on an or, so if either return true, the whole function returns true

#the sameTree function checks if the nodes are the same
#return True if both are empty

#checks if one is empty and the other is not and if the vals are the same
#return False if so outside of the if statement

#return recursive calls on the left and right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))


    def sameTree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return(self.sameTree(s.left, t.left) and 
                    self.sameTree(s.right, t.right))

        return False
