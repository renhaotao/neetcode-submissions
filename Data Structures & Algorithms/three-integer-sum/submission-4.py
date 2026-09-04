class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # def threeSum(nums):
        # print(nums)
        nums.sort()

        # print(nums)
        valid_triplets = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            if nums[i] > 0:
                break
            # else:
                # target = - nums[i]

            l = i + 1
            r = len(nums) - 1


            while l < r:
                s = nums[i] + nums[l] + nums[r]
                # print(i, l, r, s)
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    valid_triplets.append([nums[i], nums[l], nums[r]])
                    l+=1
                    while l<r and nums[l] == nums[l-1]:
                        l+= 1

        return valid_triplets

    # threeSum([-1,0,1,2,-1,-4])