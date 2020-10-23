from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowToZero = set()
        colToZero = set()
        m, n = len(matrix), len(matrix[0])
        for rowIdx in range(m):
            for colIdx in range(n):
                if matrix[rowIdx][colIdx] == 0:
                    rowToZero.add(rowIdx)
                    colToZero.add(colIdx)

        for rowIdx in range(m):
            for colIdx in range(n):
                if rowIdx in rowToZero or colIdx in colToZero:
                    matrix[rowIdx][colIdx] = 0

        return matrix

    def run(self):
        print(self.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
        print(self.setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))

foo = Solution()
foo.run()