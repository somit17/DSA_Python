import heapq
from typing import Optional

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
            
        min_heap = []
        stack = [root]
        
        # 1. Traverse all nodes and push values into the heap
        while stack:
            current = stack.pop()
            
            # Correct usage: heapq.heappush(list, item)
            heapq.heappush(min_heap, current.val)
            
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        
        # 2. Pop k-1 times to remove smaller elements
        # The k-th pop will give the k-th smallest element
        result = -1
        for _ in range(k):
            if not min_heap:
                return -1 # k is larger than number of nodes
            result = heapq.heappop(min_heap)
            
        return result