# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        #DFS Iterative
        stack = [(root,targetSum)]
        while stack:
            node , current_sum = stack.pop()

            if node.left is None and node.right is None and current_sum == node.val:
                return True
            #Append in stack
            if node.right:
                stack.append((node.right,current_sum - node.val))
            if node.left:
                stack.append((node.left,current_sum - node.val))

        return False
        