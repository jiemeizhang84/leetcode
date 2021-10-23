class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashset = set()
        for num in nums:
            if num in hashset:
                hashset.remove(num)
            else:
                hashset.add(num)
        return hashset.pop()

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res