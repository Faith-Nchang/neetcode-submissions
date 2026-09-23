class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        max_area = 0

        for i, h in enumerate(heights):

            start = i
            while stack and stack[-1][1] > h  :
                index, height = stack.pop()
                area = (i - index) * height
                max_area = max(max_area, area)
                start = index
            stack.append([start, h])

        # remaining elements
        for i, h in stack:
            max_area = max(max_area, (len(heights) - i )* h)
        return max_area

        