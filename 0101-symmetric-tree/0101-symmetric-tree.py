# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from collections import defaultdict
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        #Using BFS approach
        def bfs_approach(root: Optional[TreeNode]) -> bool:
            if not root:
                return True
            
            queue = deque([root])
            while queue:
                level_size = len(queue)
                level_values = []
                for _ in range(level_size):
                    node = queue.popleft()
                    if node:
                        level_values.append(node.val)
                        queue.append(node.left)
                        queue.append(node.right)
                    else:
                        level_values.append(None)
                # Check if level is palindrome
                if level_values != level_values[::-1]:
                    return False
            return True
        return bfs_approach(root)

        