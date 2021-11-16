class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
#         #dp = (1) Length of longest subsequence ending at this index and (2) Number of longest subsequences that end at this index. 
        dp = [[1, 1] for _ in range(len(nums))]
        longest = 1
        for i in range(len(nums)):
            cur_longest, count = 1, 0
            for j in range(i):
                if nums[j] < nums[i]:
                    cur_longest = max(cur_longest, dp[j][0] + 1)
            for j in range(i):
                if nums[j] < nums[i] and dp[j][0] == cur_longest - 1:
                    count += dp[j][1]
            dp[i] = [cur_longest, max(count, dp[i][1])]
            longest = max(longest, cur_longest)
        return sum([item[1] for item in dp if item[0] == longest])