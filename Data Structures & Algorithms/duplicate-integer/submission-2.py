class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        freq = {}

        for i in nums:
            freq[i] = 1 + freq.get(i, 0)

            if freq[i] > 1:
                return True
        
        return False 
        

        
        # if freq.keys()
       