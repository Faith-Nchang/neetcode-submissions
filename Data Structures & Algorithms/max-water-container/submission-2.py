class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_amt_water = 0

        l, r = 0, len(heights)-1

        while l < r:
            water = min(heights[l], heights[r]) * (r - l)

            max_amt_water = max(water, max_amt_water)

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1

        return max_amt_water
        