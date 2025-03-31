# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) in the tree.

# A binary search tree satisfies the following constraints:

# The left subtree of every node contains only nodes with keys less than the node's key.
# The right subtree of every node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees are also binary search trees.

# Example 1:
# Input: root = [2,1,3], k = 1
# Output: 1

# Example 2:
# # Input: root = [4,3,5,2,null], k = 4
# Output: 5

#key to this problem is inorder traversal using depth first search
#inorder traversal is left, node, right
# this will return the nodes in ascending order

#initialize a state variable to store the array that will store the bst values in order
#initialize a dfs function that will take in the root
#check if the node is empty
#return if so
#recursively call the function on the left
#append the node value to the state variable
#recursively call the function on the right
#call the dfs function with the root
#return the kth element in the state variable, since k is 1 indexed and our array is 0 indexed, we take k-1



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.resultArray = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.resultArray.append(root.val)
            dfs(root.right)

        dfs(root)
        return self.resultArray[k -1]
