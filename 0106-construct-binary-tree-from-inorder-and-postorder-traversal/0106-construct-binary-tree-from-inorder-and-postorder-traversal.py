# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder or not inorder:
            return None

        root_val = postorder.pop()
        root = TreeNode(root_val)

        index_root = inorder.index(root_val)

        left_inorder = inorder[:index_root]
        right_inorder = inorder[index_root + 1:]

        left_postorder = postorder[:len(left_inorder)]
        right_postorder = postorder[len(left_inorder):]

        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)

        return root