class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [None] * n
        pref, suf = 1, 1
        for i in range(n):
            answer[i] = pref
            pref *= nums[i]
        for j in range(n-1, -1, -1):
            answer[j] *= suf
            suf *= nums[j]
        return answer