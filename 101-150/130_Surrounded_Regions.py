from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.m = len(board)
        self.n = len(board[0])
        self.recordMap = [[0 for __ in range(self.n)] for __ in range(self.m)]
        for row_i in range(self.m):     # 左右
            if board[row_i][0] == 'O' and self.recordMap[row_i][0] == 0:
                self.walk(row_i, 0, board)
            if board[row_i][self.n - 1] == 'O' and self.recordMap[row_i][self.n - 1] == 0:
                self.walk(row_i, self.n - 1, board)

        for col_i in range(self.n):  # 上下
            if board[0][col_i] == 'O' and self.recordMap[0][col_i] == 0:
                self.walk(0, col_i, board)
            if board[self.m - 1][col_i] == 'O' and self.recordMap[self.m - 1][col_i] == 0:
                self.walk(self.m - 1, col_i, board)

        for row_i in range(self.m):
            for col_i in range(self.n):
                if board[row_i][col_i] == 'O' and self.recordMap[row_i][col_i] == 0:
                    board[row_i][col_i] = 'X'
        print(self.recordMap)
        print(board)

    def walk(self, start_i, start_j, board):
        self.recordMap[start_i][start_j] = 1
        if start_i - 1 >= 0 and self.recordMap[start_i - 1][start_j] == 0 and board[start_i - 1][start_j] == 'O':
            self.walk(start_i - 1, start_j, board)
        if start_i + 1 < self.m and self.recordMap[start_i + 1][start_j] == 0 and board[start_i + 1][start_j] == 'O':
            self.walk(start_i + 1, start_j, board)
        if start_j - 1 >= 0 and self.recordMap[start_i][start_j - 1] == 0 and board[start_i][start_j - 1] == 'O':
            self.walk(start_i, start_j - 1, board)
        if start_j + 1 < self.n and self.recordMap[start_i][start_j + 1] == 0 and board[start_i][start_j + 1] == 'O':
            self.walk(start_i, start_j + 1, board)

    def run(self):
        self.solve([["X", "X", "X", "X"], ["X", "O", "O", "X"],
                    ["X", "X", "O", "X"], ["X", "O", "X", "X"]])
        self.solve([["X"]])

foo = Solution()
foo.run()