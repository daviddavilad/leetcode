class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                old_index = stack[-1]
                stack.pop()
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                area = width * heights[old_index]
                max_area = max(max_area, area)
            stack.append(i)

        return max_area
