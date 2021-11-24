class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False

        visit = set()
        edge = { e : [] for e in range(n)}
        for i, j in edges:
            edge[i].append(j)
            edge[j].append(i)
        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for nex in edge[node]:
                dfs(nex)
        dfs(0)          
        return len(visit) == n