class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        selfless_prod = [1]
        cur_prod = 1

        for i in nums[:-1]:
            cur_prod *= i
            selfless_prod.append(cur_prod)

        cur_prod = 1

        for k in range(len(nums)-2, -1, -1):
            # k = len(nums) - j
            cur_prod *= nums[k+1]
            selfless_prod[k] *= cur_prod


        return selfless_prod
        