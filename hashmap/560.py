class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0:1}
        cnt = 0
        sm = 0
        for i in range(len(nums)):
            sm += nums[i]
            cnt += hashmap.get((sm - k), 0)
            hashmap[sm] = hashmap.get(sm, 0) + 1
        return cnt      