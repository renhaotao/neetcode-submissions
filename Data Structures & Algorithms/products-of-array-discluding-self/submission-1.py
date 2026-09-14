class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left_prod = []
        cur_prod = 1

        for i in nums[:]:
            cur_prod *= i
            left_prod.append(cur_prod)

        right_prod = []
        cur_prod = 1

        for i in nums[::-1]:
            cur_prod *= i
            right_prod.append(cur_prod)
            
        right_prod = right_prod[::-1]

        # print(right_prod)
        selfless_prod = []
        for j in range(len(nums)):
            if j == 0:
                selfless_prod.append(right_prod[j+1])
            elif j==len(nums)-1:
                selfless_prod.append(left_prod[j-1])
            else:
                selfless_prod.append(left_prod[j-1] * right_prod[j+1])


        return selfless_prod
        