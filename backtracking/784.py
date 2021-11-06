class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        
        def dfs(i, path):
            if len(path) == len(s):
                res.append(path)
                return
            
            if s[i].isalpha():
                dfs(i + 1, path + s[i].lower())
                dfs(i + 1, path + s[i].upper())
            else:
                dfs(i + 1, path + s[i])
        
        dfs(0, "")
        return res