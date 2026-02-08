# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        #Using BFS approach Will not work
        #BFS processes nodes level by level, so it finds leaves at shallower depths before deeper ones, regardless of their horizontal position.
        def bfs_approach(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if not p or not q:
                return False
            
            p_list = get_list(p)
            q_list = get_list(q)
            print(f"P >{p_list}")
            print(f"Q >{q_list}")
            return p_list == q_list
        
        #Get list logic []
        def get_list(p:Optional[TreeNode]) -> List[int]:
            if not p:
                return []
            result = []
            queue  = deque([p])
            while queue:
                node = queue.popleft()
                if not node.left and not node.right:
                    result.append(node.val)
                #print(f"----->>>>>>{node.val} and L - > {node.left} and R - > {node.right}")
                else:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

            return result

        #Using DFS
        def dfs_approach(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if not p or not q:
                return False
            return get_leaves(p)==get_leaves(q)

        def get_leaves(p:Optional[TreeNode]) -> List[int]:
            if not p:
                return []
            #Leaf Node
            if not p.left and not p.right:
                return [p.val]
            return get_leaves(p.left) + get_leaves(p.right)

        return dfs_approach(root1,root2)