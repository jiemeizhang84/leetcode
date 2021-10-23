class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        if not nums:
            return False
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False  