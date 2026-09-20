class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        LIS_list = [1] * n
        def helper():
            for i in range(n-1, -1, -1):
                if i == n-1:
                    pass
                else:
                    for j in range(i+1, n):
                        if nums[j] > nums[i]:
                            LIS_list[i] = max(1 + LIS_list[j], LIS_list[i])
                            # print(LIS_list[i])
                            # break
                # print(i, LIS_list[i])

            return max(LIS_list)

        return helper()
        