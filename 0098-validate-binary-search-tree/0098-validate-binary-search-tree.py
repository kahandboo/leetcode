# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def search(root, max, min):
            if not root:
                return True

            val = root.val

            if root.val <= min:
                return False
            if root.val >= max:
                return False

            return search(root.left, root.val, min) and search(root.right, max, root.val)
        
        return search(root, math.inf, -math.inf)
        