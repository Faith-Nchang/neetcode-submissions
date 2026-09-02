"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        old_new = {}

        def dfs(root):
            if root in old_new:
                return old_new[root]
            

            old_new[root] = Node(root.val, [])

            for n in root.neighbors:
                old_new[root].neighbors.append(dfs(n))
            return old_new[root]

        return dfs(node)