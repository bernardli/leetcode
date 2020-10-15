class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        matrix = [[0 for i in range(0, n)] for i in range(0, m)]
        rowIdx, colIdx = m - 1, n - 1
        matrix[rowIdx][colIdx] = 0
        while True:
            if rowIdx < 0 or colIdx < 0:
                break
            # right->left
            for i in range(1, colIdx + 1):
                if rowIdx + 1 == m:
                    matrix[rowIdx][colIdx - i] = 1
                else:
                    matrix[rowIdx][colIdx - i] = matrix[rowIdx +
                                                        1][colIdx - i] + matrix[rowIdx][colIdx - i + 1]
            # bottom->top
            for i in range(1, rowIdx + 1):
                if colIdx + 1 == n:
                    matrix[rowIdx - i][colIdx] = 1
                else:
                    matrix[rowIdx - i][colIdx] = matrix[rowIdx -
                                                        i][colIdx + 1] + matrix[rowIdx - i + 1][colIdx]
            rowIdx -= 1
            colIdx -= 1
            matrix[rowIdx][colIdx] = matrix[rowIdx +
                                            1][colIdx] + matrix[rowIdx][colIdx + 1]
        # print(matrix)
        return matrix[0][0]

    def run(self):
        print(self.uniquePaths(3, 2))
        print(self.uniquePaths(7, 3))
        print(self.uniquePaths(3, 7))
        print(self.uniquePaths(3, 3))
        print(self.uniquePaths(1, 5))
        print(self.uniquePaths(5, 1))
        print(self.uniquePaths(2, 2))
        print(self.uniquePaths(1, 1))


foo = Solution()
foo.run()
