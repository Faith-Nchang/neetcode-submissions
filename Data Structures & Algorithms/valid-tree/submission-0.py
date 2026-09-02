class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
         
        adj = [[] for _ in range(n)]

        for u,v  in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()

        def traverse_graph(node, parent):
            
            if node in visited:
                return False

            visited.add(node)

            for nei in adj[node]:
                if nei == parent:
                    continue

                if not traverse_graph(nei, node):
                    return False

            return True

        return traverse_graph(0, -1) and len(visited) == n
        