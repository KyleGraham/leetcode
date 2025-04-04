# Within a binary tree, a node x is considered good if the path from the root of the tree to the node x contains
# no nodes with a value greater than the value of node x

# Given the root of a binary tree root, return the number of good nodes within the tree.

# Example 1:
# Input: root = [2,1,1,3,null,1,5]
# Output: 3

# Example 2:
# Input: root = [1,2,-1,3,4]
# Output: 4


#solution using depth first search with preorder traversal

#preorder traversal - compute the logic on the node before calling the function on the left and right
# opposte is postorder traversal, call the function on the left and right then compute the logic on the node
# other is inorder traversal. Call the function on the left. Then computer the logic on the node. then call the function on the right


# in order traversal : left, node, right
# preorder traversal : node, left, right
# postorder traversal : left, right, node


#time complexity O(n)
#space complexity O(n)

#initialize a class result variable to 0 to store the result

#dfs function taking in the root and the max value
#check if the node is empty
#return if so
#do the node logic
#get the value of the node
#check if the value is greater than or equal to the max value
#increment the result variable if so
#set the new max value to the max of the current value and the max value
#recursively call the function on the left and right

#call the dfs function with the root and the root value since it can be equal
#return the result


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node, maxVal):
            if not node:
                return 
            val = node.val
            if val >= maxVal:
                self.res += 1
            newMax = max(val, maxVal)
            dfs(node.left, newMax)
            dfs(node.right, newMax)

        dfs(root, root.val)
        return self.res
