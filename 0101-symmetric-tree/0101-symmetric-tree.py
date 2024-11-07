# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSame(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSame(p.left, q.right) and self.isSame(p.right, q.left)
        

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        p = root.left
        q = root.right

        return self.isSame(p, q)
        
