class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        def dfs(node):
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return safe[node]

            visited[node] = 1
            for nei in graph[node]:
                if not dfs(nei):
                    safe[node] = False
                    break
            else:
                safe[node] = True

            visited[node] = 2
            return safe[node]

        n = len(graph)
        safe = [False]*n
        visited = [0]*n

        for index, edges in enumerate(graph):
            if not visited[index]:
                dfs(index)
        
        return [index for index in range(n) if safe[index]]