# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depthCheck(self, curr: Optional[TreeNode]) -> int:
        if not curr:
            return 0
        
        left_depth = self.depthCheck(curr.left)
        right_depth = self.depthCheck(curr.right)
        
        if left_depth == -1 or right_depth == -1:
            return -1
        
        if abs(left_depth - right_depth) > 1:
            return -1
        
        return max(left_depth, right_depth) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.depthCheck(root) != -1
