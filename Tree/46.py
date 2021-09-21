class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(dec_space, fix_path, res):
            if not dec_space:
                res.append(fix_path)
                return
            for i in range(len(dec_space)):
                dfs(dec_space[:i] + dec_space[i+1:], fix_path + [dec_space[i]], res)
            
        res = []
        dfs(nums, [], res)
        return res