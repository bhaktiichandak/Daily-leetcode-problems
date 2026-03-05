from typing import List

class Solution:
    
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        
        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        
        return max_area

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        if not matrix:
            return 0
        
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0
        
        for row in matrix:
            
            for i in range(cols):
                if row[i] == "1":
                    heights[i] += 1
                else:
                    heights[i] = 0
            
            max_area = max(max_area, self.largestRectangleArea(heights))
        
        return max_area