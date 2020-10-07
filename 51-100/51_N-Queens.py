from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.result = []
        self.n = n
        self.chessboard = [[False for i in range(n)] for i in range(n)]
        self.deepFirstSearch(0, [False for i in range(n)], [])
        return self.result

    def deepFirstSearch(self, colIdx, row, placedIndexes):
        if colIdx == self.n:
            solution = ['.' * self.n for i in range(self.n)]
            for index in placedIndexes:
                colIdx, rowIdx = index
                solution[colIdx] = solution[colIdx][:rowIdx] + 'Q' + solution[colIdx][rowIdx+1:]
            self.result.append(solution)
            return

        for rowIdx in range(self.n):
            if row[rowIdx] == True:
                continue
            if self.isNotConflicted(colIdx, rowIdx):
                self.chessboard[colIdx][rowIdx] = True
                row[rowIdx] = True
                placedIndexes.append((colIdx, rowIdx))
                self.deepFirstSearch(colIdx + 1, row, placedIndexes)
                self.chessboard[colIdx][rowIdx] = False
                row[rowIdx] = False
                placedIndexes.pop()

    def isNotConflicted(self, queenColIdx, queenRowIdx):
        colIdx = queenColIdx - 1
        rowIdx = queenRowIdx - 1
        while colIdx >= 0 and rowIdx >= 0:
            if self.chessboard[colIdx][rowIdx] == True:
                return False
            colIdx -= 1
            rowIdx -= 1

        colIdx = queenColIdx + 1
        rowIdx = queenRowIdx + 1
        while colIdx < self.n and rowIdx < self.n:
            if self.chessboard[colIdx][rowIdx] == True:
                return False
            colIdx += 1
            rowIdx += 1

        colIdx = queenColIdx - 1
        rowIdx = queenRowIdx + 1
        while colIdx >= 0 and rowIdx < self.n:
            if self.chessboard[colIdx][rowIdx] == True:
                return False
            colIdx -= 1
            rowIdx += 1

        colIdx = queenColIdx + 1
        rowIdx = queenRowIdx - 1
        while colIdx < self.n and rowIdx >= 0:
            if self.chessboard[colIdx][rowIdx] == True:
                return False
            colIdx += 1
            rowIdx -= 1
        return True

    def run(self):
        print(self.solveNQueens(4))

foo = Solution()
foo.run()