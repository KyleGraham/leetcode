# Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.
# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. 
# A node can not appear in the sequence more than once. The path does not necessarily need to include the root.
# The path sum of a path is the sum of the node's values in the path.

# Example 1:
# Input: root = [1,2,3]
# Output: 6


#optimum solution using dfs recursively
#time complexity O(n)
#space complexity O(n)

#initialize a global reult variable with the default as the value of the current root
#dfs function
#check if the root is empty
#return 0 if so
#recursively call the function on the left and right

#check if the left and right values are less than 0
#set them to 0 if so

#check if the sum of the values plus the root is greater than the cur max
#this is without splitting the left and right values, which the return can only have 1. So we're only checking against the global varaible here

#return the max of the left and right plus the root

#call the dfs function on the root
#return the result

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val

        # return max path sum without split
        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            left = max(left, 0)
            right = max(right, 0)

            # compute max path sum with split
            self.res = max(self.res, root.val + left + right)

            return root.val + max(left, right)
        dfs(root)
        return self.res