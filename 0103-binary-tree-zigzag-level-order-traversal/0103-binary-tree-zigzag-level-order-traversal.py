# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        queue = deque([root])
        level_count = 1
        while queue:
            level_size = len(queue)
            current_level = []            
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)


                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level_count % 2 == 0:
                current_level.reverse()
            result.append(current_level)
            level_count += 1

        return result