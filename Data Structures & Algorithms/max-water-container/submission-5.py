class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights)-1 

        max_vol = 0 

        while i<j:
            vol = min(heights[i], heights[j]) * (j-i)

            max_vol = max(max_vol, vol)

            if heights[i] > heights[j]:
                j -= 1 
            else:
                i += 1 

        return max_vol