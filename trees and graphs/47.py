class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(dec_space, fix_path, res):
            if not dec_space:
                res.append(fix_path)
                return
            for i in range(len(dec_space)):
                if dec_space[i] == dec_space[i-1] and i > 0:
                    continue
                dfs(dec_space[:i] + dec_space[i+1:], fix_path + [dec_space[i]], res)
            
        res = []
        nums = sorted(nums)
        dfs(nums, [], res)
        return res