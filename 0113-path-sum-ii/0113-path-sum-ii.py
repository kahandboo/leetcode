# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
result = []
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, target, path):
            if not node:
                return

            path.append(node.val)

            if not node.left and not node.right and target == node.val:
                result.append(list(path))

            dfs(node.left, target - node.val, path)
            dfs(node.right, target - node.val, path)

            path.pop()

        result = []
        dfs(root, targetSum, [])
        return result