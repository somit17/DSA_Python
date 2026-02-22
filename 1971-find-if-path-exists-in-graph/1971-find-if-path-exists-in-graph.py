from collections import defaultdict,deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #Handling edge case
        if source == destination:
            return True

        #Make adj List
        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)


        def dfs_iterative(graph,src,dest) -> bool:
            stack = [src]
            visited = set()
            while len(stack) > 0:
                current = stack.pop()
                if current == dest:
                    return True
                if current not in visited:
                    visited.add(current)
                    for neighbor in graph[current]:
                        stack.append(neighbor)

            return False

        #BFS
        def bfs_approach(graph,src,dest) -> bool:
            queue = deque([src])
            visited = set()
            while queue:
                current = queue.popleft()
                if current == dest:
                    return True
                
                if current not in visited:
                    visited.add(current)
                    for neighbor in graph[current]:
                        queue.append(neighbor)

            return False

        return bfs_approach(graph,source,destination)

    

        