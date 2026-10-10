class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        best = 0

        while l < r:
            h = min(height[l], height[r])
            best = max(best, h * (r - l))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return best
        