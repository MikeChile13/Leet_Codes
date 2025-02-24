class Solution:
    # Bob's path first
    # find the time bob reaches certain nodes
    def findBob(self, root,bob,parent):
        if bob == root:
            self.time_bob[root] = 1
            return self.time_bob[root]
        for nei in self.graph[root]:
            if nei != parent:
                time = self.findBob(nei,bob,root)
                if time:
                    self.time_bob[root] = time+1
                    return self.time_bob[root]
        return 0
    # at any point in time if Alice reaches first, she takes
    
    def findAlice(self,root,parent,current_time):
        result = float('-inf')

        # return the most profitable path to a leave node
        for nei in self.graph[root]:
            if nei != parent:
                value = self.findAlice(nei,root,current_time+1)
                result = max(result,value)

        # to compensate for the max function.
        if result == float('-inf'):
            result = 0

        if current_time < self.time_bob[root]:
            result+=self.amount[root]
        elif current_time == self.time_bob[root]:
            result += self.amount[root]//2

        # print((root,current_time,result))

        return result

    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        
        n = len(edges)+1
        # building the graph
        self.graph = defaultdict(list)
        for a,b in edges:
            self.graph[a].append(b)
            self.graph[b].append(a)

        self.time_bob = [float('inf')] * n
        self.amount = amount
        
        self.findBob(0,bob,-1)

        # print(self.time_bob)

        return self.findAlice(0,-1,1)

        