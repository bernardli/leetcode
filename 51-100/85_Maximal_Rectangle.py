from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0

        maxArea = 0
        cache = [0] * len(matrix[0])

        for rowIdx in range(len(matrix)):
            for colIdx in range(len(matrix[0])):
                if matrix[rowIdx][colIdx] == '1':
                    cache[colIdx] += 1
                else:   # matrix[rowIdx][colIdx] == 0
                    cache[colIdx] = 0
            maxArea = max(maxArea, self.largestRectangleArea(cache))
        return maxArea

    # 84题的算法
    def largestRectangleArea(self, heights: List[int]) -> int:
        left = [0] * len(heights)
        right = [0] * len(heights)
        stack = []
        maxArea = 0
        for idx in range(len(heights)):
            if len(stack) == 0:
                left[idx] = -1
                stack.append((heights[idx], idx))
            else:
                while len(stack) != 0:
                    if heights[idx] > stack[-1][0]:
                        left[idx] = stack[-1][1]
                        stack.append((heights[idx], idx))
                        break
                    else:
                        stack.pop()
                if len(stack) == 0:
                    left[idx] = -1
                    stack.append((heights[idx], idx))
        stack.clear()
        for negIdx in range(1, len(heights) + 1):
            if len(stack) == 0:
                right[-negIdx] = len(heights)
                stack.append((heights[-negIdx], len(heights) - negIdx))
            else:
                while len(stack) != 0:
                    if heights[-negIdx] > stack[-1][0]:
                        right[-negIdx] = stack[-1][1]
                        stack.append((heights[-negIdx], len(heights) - negIdx))
                        break
                    else:
                        stack.pop()
                if len(stack) == 0:
                    right[-negIdx] = len(heights)
                    stack.append((heights[-negIdx], len(heights) - negIdx))

        for idx in range(len(heights)):
            height = heights[idx]
            if height == 0:
                continue
            width = right[idx] - left[idx] - 1
            maxArea = max(maxArea, width * height)

        return maxArea

    def run(self):
        print(self.maximalRectangle([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], [
            "1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))


foo = Solution()
foo.run()
