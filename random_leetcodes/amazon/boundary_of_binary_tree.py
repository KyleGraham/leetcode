# The boundary of a binary tree is the concatenation of the root, the left boundary, 
# the leaves ordered from left-to-right, and the reverse order of the right boundary.

# The left boundary is the set of nodes defined by the following:

# The root node's left child is in the left boundary. If the root does not have a left child, then the left boundary is empty.
# If a node in the left boundary and has a left child, then the left child is in the left boundary.
# If a node is in the left boundary, has no left child, but has a right child, then the right child is in the left boundary.
# The leftmost leaf is not in the left boundary.
# The right boundary is similar to the left boundary, 
# except it is the right side of the root's right subtree. Again, the leaf is not part of the right boundary, 
# and the right boundary is empty if the root does not have a right child.

# The leaves are nodes that do not have any children. For this problem, the root is not a leaf.

# Given the root of a binary tree, return the values of its boundary.

 

# Example 1:


# Input: root = [1,null,2,3,4]
# Output: [1,3,4,2]
# Explanation:
# - The left boundary is empty because the root does not have a left child.
# - The right boundary follows the path starting from the root's right child 2 -> 4.
#   4 is a leaf, so the right boundary is [2].
# - The leaves from left to right are [3,4].
# Concatenating everything results in [1] + [] + [3,4] + [2] = [1,3,4,2].
# Example 2:


# Input: root = [1,2,3,4,5,6,null,null,null,7,8,9,10]
# Output: [1,2,4,7,8,9,10,6,3]
# Explanation:
# - The left boundary follows the path starting from the root's left child 2 -> 4.
#   4 is a leaf, so the left boundary is [2].
# - The right boundary follows the path starting from the root's right child 3 -> 6 -> 10.
#   10 is a leaf, so the right boundary is [3,6], and in reverse order is [6,3].
# - The leaves from left to right are [4,7,8,9,10].
# Concatenating everything results in [1] + [2] + [4,7,8,9,10] + [6,3] = [1,2,4,7,8,9,10,6,3].


#this question is confusing dogshit
#dfs solution
#time complexity: O(n)
#space complexity: O(h) where h is the height of the tree

#basically have to do a preorder traversal for the left side, inorder traversal for the leaves, and postorder traversal for the right side
#so we have 3 different dfs functions

#dfs leftmost
#if its a leaf node (no left or right children) we return
#otherwise we append the value to the boundary list
#and if there is a left child we call dfs leftmost on the left child
#otherwise we call dfs leftmost on the right child

#dfs leaves
#if its a leaf node we append the value to the boundary list
#otherwise we call dfs leaves on the left and right children

#dfs rightmost
#if its a leaf node we return
#if node.right exists we call dfs rightmost on the right child
#otherwise we call dfs rightmost on the left child
#and append the value to the boundary list

#finally we check if the root exists, if not, return []

#initialize boundary as an array with the root val
#if root.left
#call dfs leftmost on the left child
#call dfs leaves on the left child

#if root.right
#call dfs leaves on the right child
#call dfs rightmost on the right child
#return the boundary list


class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #preorder traversal
        def dfs_leftmost(node):
            if (not node.left) and (not node.right):
                # trick: avoid leaf nodes in this pass
                return
            boundary.append(node.val)
            if node.left:
                dfs_leftmost(node.left)
            else:
                dfs_leftmost(node.right)

        #inorder traversal
        def dfs_leaves(node):
            if (not node.left) and (not node.right):
                boundary.append(node.val)
            if node.left:
                dfs_leaves(node.left)
            if node.right:
                dfs_leaves(node.right)

        #postorder traversal
        def dfs_rightmost(node):
            if (not node.left) and (not node.right):
                return
            if node.right:
                dfs_rightmost(node.right)
            else:
                dfs_rightmost(node.left)
            boundary.append(node.val)

        if not root:
            return []
        boundary = [root.val]
        if root.left:
            dfs_leftmost(root.left)
            dfs_leaves(root.left)
        if root.right:
            dfs_leaves(root.right)
            dfs_rightmost(root.right)
        return boundary