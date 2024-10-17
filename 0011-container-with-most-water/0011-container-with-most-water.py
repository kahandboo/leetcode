class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        output = 0

        while left < right:
            w = min(height[left], height[right])
            h = right - left
            if w * h > output:
                output = w * h
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1


        return output
