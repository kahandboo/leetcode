# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        value = root.val

        if value < p.val and value < q.val and root.right:
            ret_node =self.lowestCommonAncestor(root.right, p, q)
            return ret_node

        if value > p.val and value > q.val and root.left:
            ret_node = self.lowestCommonAncestor(root.left, p ,q)
            return ret_node



        return root