class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_num = 1000000 

        for i in nums:
            min_num = min(min_num, i)

        return min_num#min(nums)