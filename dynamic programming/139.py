class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]
        
        
        
        # word_set = set(wordDict)
        # dp = [False] * (len(s) + 1)
        # dp[0] = True
        # for i in range(1, len(s) + 1):
        #     for j in range(i):
        #         if dp[j] and s[j:i] in word_set:
        #             dp[i] = True
        #             break
        # return dp[len(s)]