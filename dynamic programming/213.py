class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(nums):
            prev_prev, prev = 0, 0
            for num in nums:
                tmp = max(prev_prev + num, prev)
                prev_prev = prev
                prev = tmp
            return prev
    
        return max(helper(nums[:-1]), helper(nums[1:]), nums[0])