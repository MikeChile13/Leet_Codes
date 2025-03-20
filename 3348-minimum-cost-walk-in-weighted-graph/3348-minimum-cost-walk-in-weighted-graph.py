class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        def bfs(start):
            total_and = 131071
            q = deque()
            q.append(start)
            visited[start] = True
            while q:
                current = q.popleft()
                for nei,weight in graph[current]:
                    total_and &= weight
                    parents[nei] = start
                    if not visited[nei]:
                        q.append(nei)
                        visited[nei] = True

            return total_and
                

        maxv = 131071

        mins = [0] * n
        graph = defaultdict(list)
        parents = [i for i in range(n)]

        for i in range(len(edges)):
            u,v,weight = edges[i]
            graph[u].append((v,weight))
            graph[v].append((u, weight))

        # print(graph)
        visited= [False]*n
        for i in range(n):
            if not visited[i]:
                mins[i] = bfs(i)
        # print(mins,parents)

        res = []
        for start,end in query:
            if parents[start] != parents[end]:
                res.append(-1)
            else:
                res.append(mins[parents[start]])
        return res

        
        