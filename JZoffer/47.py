from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        if len(grid[0]) == 0:
            return 0
        dp = [[0 for __ in range(len(grid[0]) + 1)]
              for __ in range(len(grid) + 1)]
        for rowIdx in range(len(grid)):
            for colIdx in range(len(grid[0])):
                dp[rowIdx+1][colIdx+1] = max(dp[rowIdx][colIdx+1] + grid[rowIdx]
                                             [colIdx], dp[rowIdx+1][colIdx] + grid[rowIdx][colIdx])

        return dp[-1][-1]

    def run(self):
        print(self.maxValue([
            [1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]
        ]))


foo = Solution()
foo.run()
