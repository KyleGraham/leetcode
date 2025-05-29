
#solution using prefix sum
#time complexity O(n)
#space complexity O(n)

#uses a hash to store the previous values and how many times they are encountered
#then we check if the current value + root value is equal to target sum
#if so, add to res
#then add the count of the hash[cur-targetSum] to add any other options



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res = 0
        def preorder(root, cur):
            if not root:
                return
            cur += root.val
            if cur == targetSum:
                self.res += 1
            self.res += hash[cur - targetSum]
            hash[cur] += 1
            preorder(root.left, cur)
            preorder(root.right, cur)
            hash[cur] -= 1
        
        hash = defaultdict(int)
        preorder(root, 0)
        return self.res