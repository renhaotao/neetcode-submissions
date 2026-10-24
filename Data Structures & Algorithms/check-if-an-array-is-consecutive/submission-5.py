class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:


        return (len(nums) == len(set(nums)) 
                and max(nums) - min(nums) + 1 == len(nums) )
        # freq = {}

        # for i in nums:
        #     freq[i] = 1 + freq.get(i, 0)


        # return (len(freq.keys()) == len(nums) and 
        #         min(freq.keys()) + len(nums) - 1 == max(freq.keys()))
