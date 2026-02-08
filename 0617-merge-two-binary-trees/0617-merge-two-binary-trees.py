# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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

        return dfs_solution(root1,root2)
        