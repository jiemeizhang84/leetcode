class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)
        
        def dfs(path, total, start):
            if total == target:
                res.append(path.copy())
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                dfs(path, total + candidates[i], i)
                path.pop()
                
        dfs([], 0, 0)
        return res