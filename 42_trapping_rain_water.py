class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0

        for i in range(n):
            for j in range(i+1, n):
                area = min(height[i], height[j]) * (j-i-1)
                res = max(res, area)

        return res