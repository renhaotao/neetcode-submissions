# Search in Rotated Sorted Array

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums)- 1

        while l <= r:

            m = (r+l)//2
            # print(l, m, r )

            if nums[m] == target:
                return m

            if nums[r] >= nums[m]: # right monotonic
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            elif nums[m] >= nums[l]: # left monotonic
                if target < nums[m] and target >= nums[l]:
                    # print("In the left half")
                    r = m - 1
                else:
                    # print("target in the right half")
                    l = m + 1


        return - 1
        