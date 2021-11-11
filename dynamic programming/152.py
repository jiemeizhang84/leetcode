class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        max_cur, min_cur = nums[0], nums[0]
        res = max_cur
        for num in nums[1:]:
            max_tmp = max(num, max_cur * num, min_cur * num)
            min_cur = min(num, max_cur * num, min_cur * num)
            max_cur = max_tmp
            res = max(res, max_cur)
        return res