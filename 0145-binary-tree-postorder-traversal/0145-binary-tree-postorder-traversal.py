# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def Traversal(root,result):
            if not root:
                return
            
            
            if not root.left and not root.right:
                return result.append(root.val)
            
            Traversal(root.left, result)
            Traversal(root.right, result)
            
            result.append(root.val)
            


        result = []
        Traversal(root, result)

        return result