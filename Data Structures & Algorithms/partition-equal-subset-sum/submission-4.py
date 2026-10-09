class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2 == 1:
            return False

        dp = set()
        dp.add(0)
        print(dp)

        for i in nums:
            nextDP = set()
            for j in dp:
                nextDP.add(i+j)
                nextDP.add(j)
                # print(j)

            dp = nextDP

        return True if sum(nums)//2 in dp else False
        