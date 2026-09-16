class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = []

        for r in range(len(temperatures)):
            temp = temperatures[r]

            while stack and temperatures[stack[-1]] < temp:
                l = stack.pop()
                res[l] =  r - l 

            stack.append(r)
        return res
        