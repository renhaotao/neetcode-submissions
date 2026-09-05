class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        # run = 0
        print(len(nums))
        if nums[l] <= nums[r]:
            return nums[0]
        else:
            while r - l > 1:
                m = (r - l)//2 + l
                # print("l:", l, " m:", m, " r:", r)

                if nums[l] > nums[m]:
                    r = m
                elif nums[m] >= nums[r]:
                    l = m
                else:
                    return nums[0]

            # run += 1

        return nums[l+1]