from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxVol = 0

        while left != right:
            maxVol = max(min(height[left], height[right])
                         * (right - left), maxVol)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return maxVol

    def run(self):
        print(self.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))


foo = Solution()
foo.run()
