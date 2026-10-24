class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:

        freq = {}

        for i in nums:
            freq[i] = 1 + freq.get(i, 0)

        # print(freq)
        # print(min(freq.keys()) + len(nums)-1)
        # print(max(freq.keys()))

        return (len(freq.keys()) == len(nums) and 
                min(freq.keys()) + len(nums) - 1 == max(freq.keys()))

        # return False
