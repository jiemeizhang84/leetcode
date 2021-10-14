class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        max_len = 0
        hashmap = {}
        
        left = 0
        for right in range(len(s)):
            if s[right] in hashmap:
                left = max(hashmap[s[right]] + 1, left)
                
            max_len = max(max_len, right - left + 1)
            hashmap[s[right]] = right
        
        return max_len