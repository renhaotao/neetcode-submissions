class Solution:
    def rob(self, nums: List[int]) -> int:

        cache = {}
        def helper(i):

            if i >= len(nums):
                return 0
            else:
                if i not in cache:
                    cache[i] = max(nums[i] + helper(i+2), helper(i+1))
                return cache[i]

        return helper(0)
        
        # def helper(nums, cache):
        #     if len(nums) == 2:
        #         return max(nums[0], nums[1])
        #     elif len(nums) == 1:
        #         return nums[0]
        #     elif len(nums) == 0:
        #         return 0

        #     if tuple(nums) in cache:
        #         return cache[tuple(nums)]
        #     else:
        #         result = max(nums[0] + helper(nums[2:], cache), helper(nums[1:], cache))
        #         cache[tuple(nums)] = result
        #         return result

        # return helper(nums, {})
        