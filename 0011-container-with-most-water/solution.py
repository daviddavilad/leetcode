class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0

        while l < r:
            area = (r - l) * min(height[r], height[l])
            max_area = max(area, max_area)
            if height[l] >= height[r]:
                r -= 1
            else:
                l += 1
        
        return max_area