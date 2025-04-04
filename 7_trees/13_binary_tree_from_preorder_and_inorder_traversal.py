# You are given two integer arrays preorder and inorder.
# preorder is the preorder traversal of a binary tree
# inorder is the inorder traversal of the same tree
# Both arrays are of the same size and consist of unique values.
# Rebuild the binary tree from the preorder and inorder traversals and return its root.

# Example 1:
# Input: preorder = [1,2,3,4], inorder = [2,1,3,4]
# Output: [1,2,3,null,null,null,4]

# Example 2:
# Input: preorder = [1], inorder = [1]
# Output: [1]

#optimal solution using dfs
#time complexity O(n^2)
#space complexity O(n)

#what makes this problem hard is that these are not valid binary trees
#something like 2 can be on the left of a 1 node
# so you have to actually parse it from the arrays instead of just getting the head from the preorder and using the inorder value to create the tree

#check if either list is empty, return None if so
#initialize the root as the first value in the preorder list
#find the index of the root value in the inorder list, you know that values to the left of this index are on the left side of the root
#values to the right are on the right side of the root

#recursively call the function on the left side of the tree with preorder[1:mid + 1] and inorder[:mid]
  #preorder[1:mid + 1] skip first value, go up to mid
  #inorder[:mid] up to but not including mid
#return value is root.left

#recursively call the function on the right side of the tree with preorder[mid + 1:] and inorder[mid + 1:]
    #start from middle element to end on both of these
#return value is root.right

#remember we're calling these functions with the lists as params

#return the root



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        
        #preorder[1:mid + 1] skip first value, go up to mid
        #inorder[:mid] up to but not including mid
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        
        #start from middle element to end on both of these
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root