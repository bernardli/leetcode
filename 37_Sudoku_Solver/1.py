from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.sample = set([i for i in range(1, 10)])
        self.block = [[set() for i in range(3)] for i in range(3)]
        # blockIndex = [[[] for i in range(3)] for i in range(3)]
        self.row = [set() for i in range(9)]
        # rowIndex = [[] for i in range(9)]
        self.col = [set() for i in range(9)]
        # colIndex = [[] for i in range(9)]
        self.indexList = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                rowNum = i // 3
                colNum = j // 3
                char = board[i][j]
                if char == '.':
                    # blockIndex[rowNum][colNum].append((i, j))
                    # rowIndex[i].append((i, j))
                    # colIndex[j].append((i, j))
                    self.indexList.append((i, j))
                else:
                    self.block[rowNum][colNum].add(int(char))
                    self.row[i].add(int(char))
                    self.col[j].add(int(char))

        self.validPerCell(0)
            

    def validPerCell(self, emptyCellIdx):
        if emptyCellIdx >= len(self.indexList):
            return True

        rowIdx, colIdx = self.indexList[emptyCellIdx]
        candidate = self.sample - \
            self.row[rowIdx] - self.col[colIdx] - \
            self.block[rowIdx // 3][colIdx // 3]

        if len(candidate) == 0:
            return False

        for num in candidate:
            self.board[rowIdx][colIdx] = str(num)
            self.block[rowIdx // 3][colIdx // 3].add(num)
            self.row[rowIdx].add(num)
            self.col[colIdx].add(num)
            if self.validPerCell(emptyCellIdx + 1):
                return True
            else:
                self.board[rowIdx][colIdx] = '.'
                self.block[rowIdx // 3][colIdx // 3].remove(num)
                self.row[rowIdx].remove(num)
                self.col[colIdx].remove(num)
        return False

    def run(self):
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]
        self.solveSudoku(board)
        print(self.board)

foo = Solution()
foo.run()