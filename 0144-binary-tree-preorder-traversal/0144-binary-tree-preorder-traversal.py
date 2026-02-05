# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ### ROOT --> LEFT --> RIGHT

        result = []

        #Using DFS APPROACH
        def dfs(root):
            if not root:
                return 
            result.append(root.val)
            dfs(root.left)
            dfs(root.right)

        #dfs(root)

        #Using BFS
        if not root:
            return result

        stack =[root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            # Push right first so left is processed first (LIFO)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return result