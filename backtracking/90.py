class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        
        def dfs(path, start):
            res.append(path.copy())
            for i in range(start, len(nums)):
                if (i != start and nums[i] == nums[i - 1]):
                    continue
                path.append(nums[i])
                dfs(path, i + 1)
                path.pop()
        
        dfs([], 0)
        return res