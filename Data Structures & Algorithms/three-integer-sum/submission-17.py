class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums = sorted(nums)
        nums.sort()
        # print(nums)

        rtn = []
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                pass
            else:
                j, k = i+1, len(nums)-1
        
                while j < k:
        
                    if nums[j] + nums[k] == - nums[i]:
                        # print(i, j, k)
                        # if [nums[i], nums[j], nums[k]] in rtn:
                        #     pass
                        # else:
                        rtn.append([nums[i], nums[j], nums[k]])
                        j += 1 
                        k -= 1
                        while nums[k] == nums[k+1] and j<k+1:
                            k -=1 
                        while nums[j] == nums[j-1] and j-1<k:
                            j +=1 
                        # break
                    elif nums[j] + nums[k] > - nums[i]:
                        k -= 1
                    else:
                        j += 1

        return rtn