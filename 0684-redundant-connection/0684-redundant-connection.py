class UnionFind:
    def __init__(self, size = 0):
        self.parent = {i:i for i in range(1,size+1)}
        self.rank = [0]*(size+1)

    def find(self, node):
        if self.parent[node] == node:
            return node
        return self.find(self.parent[node])

    def union(self, a, b):
        parent_a = self.find(a)
        parent_b = self.find(b)
        if parent_a != parent_b:
            if self.rank[parent_a] > self.rank[parent_b]:
                self.parent[parent_b] = parent_a
            elif self.rank[parent_b] > self.rank[parent_a]:
                self.parent[parent_a] = parent_b
            else:
                self.parent[parent_b] = parent_a
                self.rank[parent_a] += 1
            return True
        else:
            return False
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = UnionFind(n)

        for u,v in edges:
            if not graph.union(u,v):
                return [u,v]
        return edges[0]

