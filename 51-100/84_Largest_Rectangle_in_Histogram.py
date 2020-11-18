from typing import List


class Solution:
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
        print(self.largestRectangleArea([2, 1, 5, 6, 2, 3]))    # 10

        print(self.largestRectangleArea([4, 2, 0, 3, 2, 4, 3, 4]))  # 10
        print(self.largestRectangleArea([5, 7, 8, 1, 1, 4, 4, 6, 5, 0, 2])) # 16

        # print(self.largestRectangleArea([6, 7, 5, 2, 4, 5, 9, 3]))


foo = Solution()
foo.run()
