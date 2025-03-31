# Given a binary tree, return true if it is height-balanced and false otherwise.
# A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# Example 1:
# Input: root = [1,2,3,null,null,4]
# Output: true

# Example 2:
# Input: root = [1,2,3,null,null,4,null,5]
# Output: false

# Example 3:
# Input: root = []
# Output: true


#solution here wants you to have the dfs function handle the bool of if its balanced
# but that makes this more complicated than it needs to be, the space for a state variable is worth it

# set a state balanced variable to True

#make a local dfs function
# if the current node is empty, return 0
# recursively call the function on the left and right
# these calls get the height of the subtrees

# if the difference between the left and right heights is greater than 1, set balanced to False

# if it's not balanced, set the state variable to false
# return the max of the left and right heights plus 1

# call the dfs function on the root
# return the state variable


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def dfs(curr):
            if not curr:
                return 0
            
            #height of the subtrees
            left = dfs(curr.left) 
            right = dfs(curr.right) 
            balanced = abs(left - right) <= 1

            if not balanced:
                self.balanced = False
            return max(left, right) + 1
        
        dfs(root)
        return self.balanced