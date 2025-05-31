# You are given the root of a binary tree.

# A ZigZag path for a binary tree is defined as follow:

# Choose any node in the binary tree and a direction (right or left).
# If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
# Change the direction from right to left or from left to right.
# Repeat the second and third steps until you can't move in the tree.
# Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

# Return the longest ZigZag path contained in that tree.

 

# Example 1:


# Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
# Output: 3
# Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
# Example 2:


# Input: root = [1,1,1,null,1,null,null,1,1,null,1]
# Output: 4
# Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).
# Example 3:

# Input: root = [1]
# Output: 0

#solution using dfs
#time complexity O(n)
#space complexity O(n) (recursion stack)

#keep track of total number of zigs and zags in self.res

#dfs has 3 params, the root, last direction traveled, and count of zigzags

#check if root is null
#set res to max of self and count
#if last dir is right, call dfs on left with left as last dir and count + 1
#also call dfs on right with right and 1 as count since it went wrong direction

#same thing in reverse if last dir is left

#call dfs on root, right, 0 (initial direction doesn't matter)
#return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root, dir, count):
            if root:
                self.res = max(count, self.res)
                if dir == 'right':
                    dfs(root.left, 'left', count + 1)
                    dfs(root.right, 'right', 1)
                else:
                    dfs(root.right, 'right', count + 1) 
                    dfs(root.left, 'left', 1)
        dfs(root, 'right' , 0)
        return self.res