class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        # print(intervals)

        output = [intervals[0]]

        for [start, end] in intervals[1:]:
            if start > output[-1][1]:
                # no overlap
                output.append([start, end])
            else:
                output[-1][0] = min(output[-1][0], start)
                output[-1][1] = max(output[-1][1], end)
                
        return output