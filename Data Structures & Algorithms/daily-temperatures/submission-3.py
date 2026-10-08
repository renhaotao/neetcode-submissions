class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        stack = [] # [temp, idx]
        for i in range(n):
            while len(stack) != 0 and temperatures[i] > stack[-1][0]:
                tempT, tempIdx = stack.pop()
                res[tempIdx] = i - tempIdx
                

            stack.append([temperatures[i], i])

        
        return res

