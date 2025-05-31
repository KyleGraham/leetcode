
#soluton using bfs
#time complexity O(n)
#space complexity O(n)

#just go through every node at every level and calc the sum
#make sure to check if left or right exist before adding them to the q, since an empty level will check the max against the default 0
#return the level containing the max sum. Root is level 1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')
        res = 0
        q = deque([root])
        counter = 0
        while q:
            counter += 1
            val = 0
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    val += node.val
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if val > maxSum:
                maxSum = val
                res = counter
        return res