class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        previous_val = nums[0]
        num_unique = 1

        total_size = len(nums)

        i = 1 
        while i < total_size:
            print("nums", i, nums)

            next_val = nums[i]
            print("previous_val", previous_val, "next_val",next_val)

            if next_val == previous_val:
                # Shift to the left the array from i to len(nums) by 1 
                print("Found duplicate")
                print("Shifting array", i, len(nums)-1,"to left by 1")
                for j in range(i, len(nums)-1):
                    nums[j] = nums[j+1]
                nums[-1] = 0

                total_size -= 1 
            else:
                num_unique += 1 
                i += 1 


            previous_val = next_val

            print("num_unique",num_unique)



        return num_unique

#sol = Solution()

#sol.removeDuplicates([1, 1, 2, 3, 4])