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
        if not root:
            return True
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
        #Using DFS approach we will pass subtree only
        def dfs_approach(left: Optional[TreeNode],right:Optional[TreeNode]) -> bool:
            if not left and not right:
                return True
            if not left or not right:
                return False
            
            return left.val==right.val and dfs_approach(left.left,right.right) and dfs_approach(left.right,right.left)
        
        #return bfs_approach(root)
        return dfs_approach(root.left,root.right)

        