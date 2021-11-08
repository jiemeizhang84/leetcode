class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        visited = [False] * len(nums)
        
        def dfs(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for i in range(len(nums)):
                if ((visited[i] ) or (i > 0 and nums[i] == nums[i - 1] and not visited[i - 1])):
                    continue
                visited[i] = True
                path.append(nums[i])
                dfs(path)
                visited[i] = False
                path.pop()

        dfs([])
        return res