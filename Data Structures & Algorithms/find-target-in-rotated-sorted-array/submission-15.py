# Search in Rotated Sorted Array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # print()
        l, r = 0, len(nums)-1
        m = (l+r)//2

        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1

        if len(nums) == 2:
            for k in range(len(nums)):
                if target == nums[k]:
                    return k
            return -1


        # while r-l>2:
        while m != l and m != r:
        # for p in range(3):
            m = (l+r)//2

            # print("l: {}, m: {}, r: {}".format(l, m, r))
            # print("n[l]: {}, n[m]:, n[r]: {}".format(nums[l], nums[m], nums[r]))
            # print("n[l]:n[r]: {}".format(nums[l:(r+1)]))

            if target >= nums[m]:
                # print("tar {} >= num[{}]: {}".format(target, m, nums[m]))
                # check if m is target
                if target == nums[m]:
                    return m

                if nums[m] > nums[l]:  # check if left is monotonic
                    l = m+1
                elif nums[r] > nums[m]: # check if right is monotonic
                    if target > nums[r]:
                        r = m -1
                    elif target < nums[r]:
                        l = m+1
                    else:
                        return r

            if target < nums[m]:
                # print("tar {} < num[{}]: {}".format(target, m, nums[m]))

                if nums[m] >= nums[l]: # left is monotonic
                    if target > nums[l]:
                        r = m-1
                    elif target < nums[l]:
                        l = m + 1
                    else:
                        return l
                elif nums[m] < nums[r]:
                    # if target == nums[r]:
                    #     return r
                    # else:
                    r = m-1
                else:
                    return -1
        return -1

        # return 1