class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # if len(nums) == 1 and target == nums[0]:
        #     return 0

        l, r = 0, len(nums)-1

        while l <= r:
            m = (r - l) // 2 + l
            # print(l, m, r )

            if nums[m] == target:
                return m
            elif nums[m]<target:
                l = m + 1
            else:
                r = m - 1

            # if nums[l] == target:
            #     return l

        return - 1