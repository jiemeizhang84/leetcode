class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def dfs(path, start):
            if start == len(s):
                res.append(path.copy())
                return
            for i in range(start, len(s)):
                if self.is_palindrome(s, start, i):
                    path.append(s[start: i + 1])
                    dfs(path, i + 1)
                    path.pop()
       
        dfs([], 0)
        return res        
        
    def is_palindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True