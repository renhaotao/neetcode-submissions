class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        # i, j = 0, len(nums)-1
        # print(i, j)

        # while i < j:

        #     cur_sum = nums[i] + nums[j]
        #     print("cur_sum:", cur_sum)

        #     if cur_sum > target:
        #         j -= 1 
        #     elif cur_sum < target:
        #         i += 1 
        #     else:
        #         return [i, j]

        