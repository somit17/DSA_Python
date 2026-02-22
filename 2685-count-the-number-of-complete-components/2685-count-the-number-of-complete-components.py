from collections import defaultdict
from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * n
        complete_count = 0
        
        def dfs(node, component):
            visited[node] = True
            component.append(node)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor, component)
        
        for i in range(n):
            if not visited[i]:
                component = []
                dfs(i, component)
                
                # Check if this component is complete
                # In a complete graph with k nodes, each node has degree k-1
                # Total edges = k * (k-1) / 2
                k = len(component)
                expected_edges = k * (k - 1) // 2
                actual_edges = sum(len(graph[node]) for node in component) // 2
                
                if actual_edges == expected_edges:
                    complete_count += 1
        
        return complete_count