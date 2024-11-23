# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def Traversal(root, result):
            if not root:
                return 0

            result = result*10
            result += root.val

            if not root.left and not root.right:
                return result

            left = Traversal(root.left, result)
            right = Traversal(root.right, result)

            return left + right

        return Traversal(root, 0)

