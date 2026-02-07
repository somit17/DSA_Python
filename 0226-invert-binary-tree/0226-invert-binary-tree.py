# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        #DFS approcach
        def solve(node:Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return None
            
            left_inverted = solve(node.left)
            right_inverted = solve(node.right)

            #Swap child
            node.left = right_inverted
            node.right = left_inverted
            
            return node

            #Using BFS approach
        def solve_bfs(root:Optional[TreeNode]) -> Optional[TreeNode]:
                if not root:
                    return None
                
                queue = deque([root])
                while queue:
                    node = queue.popleft()

                    left = node.left
                    right = node.right

                    #Swap 
                    node.left = right
                    node.right = left

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

                return root
        return solve_bfs(root)
        