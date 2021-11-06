class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        
        for num in nums:
            if num - 1 not in num_set:
                cur_len = 1
                while (num + cur_len) in num_set:
                    cur_len += 1
                longest = max(longest, cur_len)
        return longest