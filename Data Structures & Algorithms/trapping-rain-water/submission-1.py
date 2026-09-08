class Solution:
    def trap(self, height: List[int]) -> int:
        

        l,r = 0, len(height) - 1

        maxHeight_Left = height[l]
        maxHeight_Right = height[r]
        res = 0

        while l < r:

            if maxHeight_Left < maxHeight_Right:
                l += 1
                maxHeight_Left = max(maxHeight_Left, height[l])
                res += maxHeight_Left - height[l]

            else:
                r-=1
                maxHeight_Right = max(maxHeight_Right, height[r])
                res += maxHeight_Right - height[r]
        return res


        