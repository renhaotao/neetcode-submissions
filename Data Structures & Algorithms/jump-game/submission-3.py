class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        dp = {}
        def helper(i):
            # print(i)
            if i not in dp:
                if i == n-1:
                    # dp[i] = False
                    return True
                elif i > n-1:
                    return False
                elif nums[i] == 0 and i != n-1:
                    # dp[i] = True
                    return False
                else:
                    max_step = nums[i]
                    dp[i] = any([helper(i+j) for j in range(1, max_step+1)])

                return dp[i]

        ans = helper(0)

        return ans

        