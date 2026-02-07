# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #Using DFS Approach
        def is_same_dfs(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            
            if not p or not q:
                return False

            if p.val!=q.val:
                return False
            
            return is_same_dfs(p.left,q.left) and is_same_dfs(p.right,q.right)

        #Using BFS approach
        def same_tree_bfs(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            queue = deque([(p,q)])

            while queue:
                node1,node2 = queue.popleft()

                if not node1 and not node2:
                    continue
                if not node1 or not node2:
                    return False
                if node1.val != node2.val:
                    return False

                queue.append((node1.left,node2.left))
                queue.append((node1.right,node2.right))
            return True   
        
        #return is_same_dfs(p,q)
        return same_tree_bfs(p,q)
        