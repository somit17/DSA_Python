# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        #DFS Approach 
        def dfs_solution(p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
            if not p and not q:
                return None
            v1 = p.val if p else 0
            v2 = q.val if q else 0
            root = TreeNode(v1+v2)
            root.left = dfs_solution(p.left if p else None,q.left if q else None)
            root.right = dfs_solution(p.right if p else None,q.right if q else None)
            return root

        #BFS APPROACH
        def bfs_solution(p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
            if not p and not q:
                return None
            
            root = TreeNode((p.val if p else 0)+(q.val if q else 0))
            queue = deque([(p,q,root)])

            #LOGIC
            while queue:
                node1, node2, merged = queue.popleft()

                #Handle left children
                left1 = node1.left if node1 else None
                left2 = node2.left if node2 else None
                
                if left1 and left2:
                    merged.left = TreeNode(left1.val+left2.val)
                    queue.append((left1,left2,merged.left))
                elif left1:
                    merged.left = left1
                elif left2:
                    merged.left = left2

                #Handle Right children
                right1 = node1.right if node1 else None
                right2 = node2.right if node2 else None
                
                if right1 and right2:
                    merged.right = TreeNode(right1.val+right2.val)
                    queue.append((right1,right2,merged.right))
                elif right1:
                    merged.right = right1
                elif right2:
                    merged.right = right2

            return root
        #return dfs_solution(root1,root2)
        return bfs_solution(root1,root2)
        