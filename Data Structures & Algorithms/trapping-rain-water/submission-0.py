class Solution:
    def trap(self, height: List[int]) -> int:
        maxL, maxR = [0] * len(height), [0] * len(height)
        n = len(height)
        for i in range(1, n):
            maxL[i] = max(maxL[i-1], height[i-1])

        for i in range(n-2, -1, -1):
            maxR[i] =  max(maxR[i+1], height[i+1])
        
        print(maxL)
        print(maxR)
        max_s = 0
        for j in range(n):
            max_s += max(0, min(maxL[j], maxR[j]) - height[j])

        return max_s

        