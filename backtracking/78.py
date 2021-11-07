class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        self.dfs(nums, subset, res, 0)
        return res        
        
    def dfs(self, nums, subset, res, i):
        if i >= len(nums):
            res.append(subset.copy())
            return
        subset.append(nums[i])
        self.dfs(nums, subset, res, i + 1)
        subset.pop()
        self.dfs(nums, subset, res, i + 1)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(path, i):
            if i >= len(nums):
                res.append(path.copy())
                return
            # path.append(nums[i])
            dfs(path, i + 1)
            path.append(nums[i])
            dfs(path, i + 1)
            path.pop()
                    
        dfs([], 0)
        return res