from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return grid[0][0]
        
        longest = [[0 for i in range(0, n)] for i in range(0, m)]
        rowIdx, colIdx = m - 1, n - 1
        longest[rowIdx][colIdx] = grid[rowIdx][colIdx]
        while True:
            if rowIdx < 0 or colIdx < 0:
                break
            # right->left
            for i in range(1, colIdx + 1):
                if rowIdx + 1 == m:
                    longest[rowIdx][colIdx - i] = grid[rowIdx][colIdx -
                                                               i] + longest[rowIdx][colIdx - i + 1]
                else:
                    longest[rowIdx][colIdx - i] = min(longest[rowIdx + 1][colIdx - i],
                                                      longest[rowIdx][colIdx - i + 1]) + grid[rowIdx][colIdx - i]
            # bottom->top
            for i in range(1, rowIdx + 1):
                if colIdx + 1 == n:
                    longest[rowIdx - i][colIdx] = grid[rowIdx -
                                                       i][colIdx] + longest[rowIdx - i + 1][colIdx]
                else:
                    longest[rowIdx - i][colIdx] = min(longest[rowIdx - i + 1][colIdx],
                                                      longest[rowIdx - i][colIdx + 1]) + grid[rowIdx - i][colIdx]
            rowIdx -= 1
            colIdx -= 1
            longest[rowIdx][colIdx] = min(
                longest[rowIdx + 1][colIdx], longest[rowIdx][colIdx + 1]) + grid[rowIdx][colIdx]
        # print(matrix)
        # print(longest)
        return longest[0][0]

    def run(self):
        print(self.minPathSum([
            [1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]
        ]))


foo = Solution()
foo.run()
