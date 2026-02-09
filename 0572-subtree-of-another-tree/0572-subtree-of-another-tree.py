# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def dfs_approach(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            if not root:
                return False
            if not subRoot:
                return True
            
            if is_same_tree(root,subRoot):
                return True

            return (dfs_approach(root.left,subRoot) or dfs_approach(root.right,subRoot))

        def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
                if not p and not q:
                    return True
                if not p or not q:
                    return False

                if p and q and p.val == q.val:
                    return is_same_tree(p.left,q.left) and is_same_tree(p.right,q.right)
        
        return dfs_approach(root,subRoot)
        