class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0

        dp_1 = nums[-1]       # i = n-1
        dp_2 = max(nums[-2:]) # i = n-2

        for i in range(len(nums)-3, -1, -1):
            dp_2_new = max(nums[i]+dp_1, dp_2)
            dp_1 = dp_2
            dp_2 = dp_2_new

        return dp_2

        # dp = dict()
        # def helper(nums):

        #     if tuple(nums) not in dp:
        #         if len(nums) <= 2:
        #             dp[tuple(nums)] = max(nums)
        #         else:
        #             dp[tuple(nums)] = max(nums[0] + helper(nums[2:]), helper(nums[1:]))

        #     return dp[tuple(nums)]

        # return helper(nums)

        # def helper(nums):
        #     if len(nums) <= 2:
        #         return max(nums)

        #     return max(nums[0] + helper(nums[2:]), helper(nums[1:]))

        # return helper(nums)