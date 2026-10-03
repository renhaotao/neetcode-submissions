class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        # global_sum = 0

        for i in range(len(nums)):
            # print(i, cur_sum)
            if cur_sum < 0:
                cur_sum = nums[i]
            else:
                cur_sum += nums[i]

            if i == 0:
                global_sum = nums[i]

            global_sum = max(global_sum, cur_sum)
            # print("global_sum:", global_sum)
        return global_sum

      