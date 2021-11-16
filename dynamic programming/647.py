class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            l, r = i, i
            while l <= r and l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            l, r = i, i + 1
            while l <= r and l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res

#DP
class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        res = 0
        if N == 0: return res
        dp = [[False] * N for _ in range(N)]
        print(dp)
        for i in range(N):
            dp[i][i] = True
            res += 1
        for i in range(N - 1):
            dp[i][i + 1] = s[i] == s[i + 1]
            res += 1 if dp[i][i + 1] else 0
            
        for length in range(2, N):
            for i in range(N - length):
                dp[i][i + length] = dp[i + 1][i + length - 1] and s[i] == s[i + length]
                res += 1 if dp[i][i + length] else 0
                
        return res