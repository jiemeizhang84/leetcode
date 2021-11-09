class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_prev, prev = 0, 0
        for num in nums:
            tmp = max(prev_prev + num, prev)
            prev_prev = prev
            prev = tmp
        return prev