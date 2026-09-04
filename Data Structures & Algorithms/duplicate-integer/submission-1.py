class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False

        nums_sort = nums.copy()
        nums_sort.sort()

        last_val = nums_sort[0]

        for val in nums_sort[1:]:
            if val == last_val:
                return True
            last_val = val
            
        return False
        