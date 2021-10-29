class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        result = deque([])
        while left <= right:
            if nums[left]**2 > nums[right]**2:
                result.appendleft(nums[left]**2)
                left += 1
            else:
                result.appendleft(nums[right]**2)
                right -= 1
        return result