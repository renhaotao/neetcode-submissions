class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod  = [0] * len(nums)
        postfix_prod = [1] * len(nums)
        result = [0] * len(nums)

        running_prod = 1
        for i in range(len(nums)):
            running_prod *= nums[i]
            prefix_prod[i] = running_prod

        running_prod = 1
        for i in range(len(nums)-2, -1, -1):
            running_prod *= nums[i+1]
            postfix_prod[i] = running_prod

        result[0] = postfix_prod[0]
        for j in range(1, len(nums)):
            result[j] = prefix_prod[j-1] * postfix_prod[j]

        return result