# Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.
# Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:
# Input: p = [4,7], q = [4,null,7]
# Output: false

# Example 3:
# Input: p = [1,2,3], q = [1,3,2]
# Output: false


#solution using recursive depth first search
#time complexity O(n)
#space complexity O(n)

#initialize a state variable to store the result

#dfs function taking in both trees
#check if both trees are empty
#return if so

#check if one of the trees is empty and the other is not
# set state variable to false and return if so

#check if the nodes are not equal
#set state variable to false and return

#recursively call the function on the left and right

# call the dfs function with both trees
# return the state variable

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.even = True
        def dfs(p, q):
            if not p and not q:
                return
            if p and not q or q and not p:
                self.even = False
                return
            if p.val != q.val:
                self.even = False
                return
            dfs(p.left, q.left)
            dfs(p.right, q.right)

        dfs(p, q)
        return self.even