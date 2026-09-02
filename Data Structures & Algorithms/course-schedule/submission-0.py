class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacency_lst = {i:[] for i in range(numCourses)}

        for crs, preq in prerequisites:
            adjacency_lst[crs].append(preq)

        visited = set()
        def dfs(crs):
            if crs in visited:
                return False

            if adjacency_lst[crs] == []:
                return True

            visited.add(crs)
            for preq in adjacency_lst[crs]:
                if not dfs(preq):
                    return False
            visited.remove(crs)
            adjacency_lst[crs] = []
            return True

        for crs in adjacency_lst:
            if not dfs(crs):
                return False
        return True