class Solution:
    def maxArea(self, heights: List[int]) -> int:

        i = 0
        j = len(heights)-1

        max_area = 0
        
        print(i, j, max_area)

        while i < j:
            area = (j-i) * min(heights[j], heights[i])
            max_area = max(area, max_area)
            # print(i, j, max_area)

            if heights[i] < heights[j]:
                i += 1
            elif heights[i] >= heights[j]:
                j -= 1 

        return max_area
             

        
        # current = (len(heights)-1) * min(heights[-1], heights[0])

        # imax, jmax = 0, len(heights)-1
        # area_max = 0

        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         area = (j - i) * min(heights[j], heights[i])
        #         # print(i, j, area, current)
        #         if area >= current:
        #             imax, jmax = i, j
        #             area_max = area

        #             current = area 

        # return area_max
    
