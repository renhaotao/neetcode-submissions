class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1

        while l <= r:
            m = (r - l)//2 + l

            if nums[m] < target:
                l = m + 1
            elif nums[m] >= target:
                r = m - 1

        # if r - l == -1:
        #    lower = -1
        # else:
        lower = l


        l, r = 0, len(nums)-1

        while l <= r:
            m = (r - l)//2 + l

            if nums[m] <= target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1

        # upper = m
        # if r - l == -1:
        #     upper = -1
        # else:
        upper = r
        
        if upper - lower == -1:
            return [-1, -1]
        else:
            return [lower, upper]