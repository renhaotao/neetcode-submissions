class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res = -float('inf')
        curSum = 0

        for i in range(len(nums)):
            curSum += nums[i]
            
            if curSum < nums[i]:
                curSum = nums[i]

            res = max(curSum, res)

        return res