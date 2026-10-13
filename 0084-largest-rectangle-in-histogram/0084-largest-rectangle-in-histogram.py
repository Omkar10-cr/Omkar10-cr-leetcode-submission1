class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []  # indices with increasing heights
        best = 0
        heights = heights + [0]  # sentinel to flush the stack

        for j in range(len(heights)):
            while stack and heights[stack[-1]] > heights[j]:
                h = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = j - left - 1
                best = max(best, h * width)
            stack.append(j)

        return best