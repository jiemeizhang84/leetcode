class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def dfs(r, c, visited, prev_height):
            if (r, c) in visited or r < 0 or c < 0 or r == ROW or c == COL or heights[r][c] < prev_height:
                return
            visited.add((r, c))
            for i, j in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                dfs(r + i, c + j, visited, heights[r][c])
                
        for c in range(COL):
            dfs(0, c, pac, 0)
            dfs(ROW - 1, c, atl, 0)
        
        for r in range(ROW):
            dfs(r, 0, pac, 0)
            dfs(r, COL - 1, atl, 0)
            
        res = []
        for r in range(ROW):
            for c in range(COL):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res