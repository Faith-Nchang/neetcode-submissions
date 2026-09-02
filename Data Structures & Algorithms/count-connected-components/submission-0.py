class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        visited = set()

        adj = [[] for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        
        def dfs(node):
            for ne in adj[node]:
                if ne not in visited:
                    visited.add(ne)
                    dfs(ne)
        
        res = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                res += 1
        return res