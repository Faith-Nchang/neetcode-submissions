class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        max_area = 0

        for r in range(len(heights) + 1):

            while stack and (r == len(heights) or heights[stack[-1]] >= heights[r]):
                left = stack.pop()
                height = heights[left]
                width = r if not stack else r - stack[-1] - 1
                area = width * height
                max_area = max(max_area, area)
            
            stack.append(r)

        return max_area

        