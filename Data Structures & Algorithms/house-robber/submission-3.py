class Solution:
    def rob(self, nums: List[int], cache={}) -> int:
        if len(nums) == 2:
            return max(nums[0], nums[1])
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 0:
            return 0

        if tuple(nums) in cache:
            return cache[tuple(nums)]
        else:
            result = max(nums[0] + self.rob(nums[2:], cache), self.rob(nums[1:], cache))
            cache[tuple(nums)] = result
            return result
        