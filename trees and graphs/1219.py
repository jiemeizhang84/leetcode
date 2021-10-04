class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        def dfs(i, j, sum, seen):
            if i<0 or i>=m or j<0 or j>=n or not grid[i][j] or (i,j) in seen:
                return sum
            seen.add((i, j))
            sum += grid[i][j]
            max_gold = 0
            for x, y in ((i, j+1), (i, j-1), (i+1, j), (i-1, j)):
                max_gold = max(dfs(x, y, sum, seen), max_gold)
            seen.discard((i, j))
            return max_gold
        
        m, n = len(grid), len(grid[0])
        return max(dfs(i, j, 0, set()) for j in range(n) for i in range(m))
        