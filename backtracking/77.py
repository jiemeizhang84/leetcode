class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def dfs(path, start):
            if len(path) == k:
                res.append(path.copy())
                return
            for i in range(start, n + 1):
                path.append(i)
                dfs(path, i + 1)
                path.pop()
        
        dfs([], 1)
        return res