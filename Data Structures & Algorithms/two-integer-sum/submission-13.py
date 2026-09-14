class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        md = dict()

        for i in range(len(nums)):
            inverse = target - nums[i]
            
            # print(i, md, md.get(inverse), inverse)
            if md.get(inverse) is None:
                md[nums[i]] = i
            else:
                return [min(i, md[inverse]), max(i, md[inverse])]

        