class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height)-1
        max_water = 0

        while start < end:
            width = end - start
            max_height = min(height[start], height[end])

            if width * max_height > max_water:
                max_water = width * max_height
            
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        
        return max_water