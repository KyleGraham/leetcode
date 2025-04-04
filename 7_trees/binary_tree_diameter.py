# The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree. 
# The path does not necessarily have to pass through the root.
# The length of a path between two nodes in a binary tree is the number of edges between the nodes.
# Given the root of a binary tree root, return the diameter of the tree.

# Example 1:
# Input: root = [1,null,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [1,2,3,5] or [5,3,2,4].

# Example 2:
# Input: root = [1,2,3]
# Output: 2

# optimal solution using recursive depth first search
# time complexity O(n)
# space complexity O(n)

# initialize instance variable to store the result

# dfs function
# check if the current node is empty
# return 0 if so
# recursively call the function on the left and right
# these calls get the height of the subtrees

#update res if the sum of the left and right heights is greater than the current res
#return the max of the left and right heights plus 1

#call the dfs function on the root
#return the result


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        # returns height
        def dfs(curr):
            if not curr:
                return 0
            #height of the subtrees
            left = dfs(curr.left)
            right = dfs(curr.right)
            

            self.res = max(self.res, (left + right))
            return max(left, right) + 1 #adds 1 for the root
        dfs(root)
        return self.res