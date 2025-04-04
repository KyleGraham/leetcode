# You are given the root of a binary tree. 
# Return only the values of the nodes that are visible from the right side of the tree, ordered from top to bottom.

# Example 1:
# Input: root = [1,2,3]
# Output: [1,3]

# Example 2:
# Input: root = [1,2,3,4,5,6,7]
# Output: [1,3,7]

#optimal solution using bredth first search
#time complexity O(n)
#space complexity O(n)

#basically, you have a person on the right side of a binary tree, and you have to return the nodes that person can see

#initialize an empty list to store the right side view
#initialize a deque with the root
#while the deque is not empty
#initialize a variable to store the right side view to None
#initialize a variable to store the length of the deque, this will be the length of the layer

#loop through the length of the layer
#pop the leftmost node
#if the node exists, set the right side view to the node
#append the left and right children

#since we're traversing the queue from left to right, the rightmost node will always be the right mode node in the layer
#append the right side view to the result if it exists
#return the result


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])
        
        while q:
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val) 
        return res

