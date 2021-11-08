class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        res = []
        def dfs(path, total, start):
            if (total == n) and (len(path) == k):
                res.append(path.copy())
                return
            if (total > n) or (len(path) > k):
                return
            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(path, total + nums[i], i + 1)
                path.pop()
                
        dfs([], 0, 0)
        return res