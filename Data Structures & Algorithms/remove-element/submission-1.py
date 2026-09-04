class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) > 0:
            prev_val = nums[0]

            i = 0

            total_size = len(nums)

            while i < total_size:
                if nums[i] == val:

                    for j in range(i, len(nums)-1):
                        nums[j] = nums[j+1]
                    nums.pop()
                    total_size -= 1
                else:
                    i += 1 
        else:
            pass

        return len(nums)
        