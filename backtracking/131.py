class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, [], res, 0)
        return res
        
    def dfs(self, s, part, res, i):
        if i >= len(s):
            res.append(part.copy())
            return
        for j in range(i, len(s)):
            if self.is_palindrome(s, i, j):
                part.append(s[i:j+1])
                self.dfs(s, part, res, j+1)
                part.pop()
        
        
    def is_palindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True