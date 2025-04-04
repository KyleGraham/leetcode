# Given the root of a binary tree, return true if it is a valid binary search tree, otherwise return false.
# A valid binary search tree satisfies the following constraints:
# The left subtree of every node contains only nodes with keys less than the node's key.
# The right subtree of every node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees are also binary search trees.

# Example 1:
# Input: root = [2,1,3]
# Output: true

# Example 2:
# Input: root = [1,2,3]
# Output: false

#optimal solution using depth first search
#time complexity O(n)
#space complexity O(n)

#initialize a state variable to store the result

#create valid function taking in the node, the left and right values that will act as our dfs function
#check if the node is empty
#return if so
#check if the node value is greater than the left and less than the right
#set the state variable to false if not
#recursively call the function on the left and right
#tricky part here is that we have to factor in the nodes value in the comparison
#so to check the left node, we pass the current value of left and the node value as the right
#to check the right node, we pass the node value as the left and the current value of right

#when calling the function initially, we pass negative infinity and positive infinity as the left and right values
#this is because thats what the root node will be compared to
#return the state variable


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.validBst = True 

        def valid(node, left, right):
            if not node:
                return
            if not (node.val < right and node.val > left):
                self.validBst = False
            valid(node.left, left, node.val)
            valid(node.right, node.val, right)

        valid(root, float('-infinity'), float('infinity'))
        return self.validBst