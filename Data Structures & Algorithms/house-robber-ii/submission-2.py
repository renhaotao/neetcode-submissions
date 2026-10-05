class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_linear(nums):

            if not nums:
                return 0

            dp_1 = nums[-1]       # i = n-1
            dp_2 = max(nums[-2:]) # i = n-2

            for i in range(len(nums)-3, -1, -1):
                dp_2_new = max(nums[i]+dp_1, dp_2)
                dp_1 = dp_2
                dp_2 = dp_2_new

            return dp_2

        if len(nums) == 1:
            return max(nums)
        else:
            return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))
