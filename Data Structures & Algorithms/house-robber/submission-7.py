class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = dict()
        def helper(nums):

            if tuple(nums) not in dp:
                if len(nums) <= 2:
                    dp[tuple(nums)] = max(nums)
                else:
                    dp[tuple(nums)] = max(nums[0] + helper(nums[2:]), helper(nums[1:]))

            return dp[tuple(nums)]

        return helper(nums)

        # def helper(nums):
        #     if len(nums) <= 2:
        #         return max(nums)

        #     return max(nums[0] + helper(nums[2:]), helper(nums[1:]))

        # return helper(nums)