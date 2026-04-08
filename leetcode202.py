#684. Redundant Connection
class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        parent = list(range(len(edges) + 1))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False 
            parent[rootY] = rootX
            return True

        ans = []
        for u, v in edges:
            if not union(u, v):
                ans = [u, v]  

        return ans