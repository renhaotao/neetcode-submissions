class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
       
        n = len(nums)
        dp = [1]*n

        for j in range(1, n):
            dp[j] = max(([dp[i] + 1 for i in range(0, j) if nums[j] > nums[i]]) , default=1)

        # print(dp)

        return max(dp)