class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        def bfs(start,graph):
            q = deque([start])
            edges = 0
            nodes = 1
            visited[start] = 1
            while q:

                current = q.popleft()

                for nei in graph[current]:
                    if visited[nei] == 2:
                        continue
                    
                    if visited[nei] == 0:
                        visited[nei] = 1
                        q.append(nei)
                        nodes += 1
                    edges += 1
                visited[current] = 2

            return (nodes,edges)

        graph = defaultdict(list)
        complete_cmp = 0
        visited = [0]*n

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        for i in range(n):
            
            if visited[i] == 0:
                nodes,edges = bfs(i,graph)
                # print(i,nodes,edges)
                if edges == nodes * (nodes - 1)//2:
                    complete_cmp += 1
        
        return complete_cmp



