from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.result = []
        self.n = n
        self.chessboard = [[False for i in range(n)] for i in range(n)]
        self.deepFirstSearch(0, [False for i in range(n)], [])
        return self.result

    def deepFirstSearch(self, rowIdx, collumStatus, placedIndexes):
        if rowIdx == self.n:
            solution = ['.' * self.n for i in range(self.n)]
            for index in placedIndexes:
                rowIdx, colIdx = index
                solution[rowIdx] = solution[rowIdx][:colIdx] + 'Q' + solution[rowIdx][colIdx+1:]
            self.result.append(solution)
            return
        

        for colIdx in range(self.n):
            if collumStatus[colIdx] == True:
                continue
            if self.isNotConflicted(rowIdx, colIdx):
                self.chessboard[rowIdx][colIdx] = True
                collumStatus[colIdx] = True
                placedIndexes.append((rowIdx, colIdx))
                self.deepFirstSearch(rowIdx + 1, collumStatus, placedIndexes)
                self.chessboard[rowIdx][colIdx] = False
                collumStatus[colIdx] = False
                placedIndexes.pop()

    def isNotConflicted(self, queenColIdx, queenRowIdx):
        rowIdx = queenColIdx - 1
        colIdx = queenRowIdx - 1
        while rowIdx >= 0 and colIdx >= 0:
            if self.chessboard[rowIdx][colIdx] == True:
                return False
            rowIdx -= 1
            colIdx -= 1

        rowIdx = queenColIdx + 1
        colIdx = queenRowIdx + 1
        while rowIdx < self.n and colIdx < self.n:
            if self.chessboard[rowIdx][colIdx] == True:
                return False
            rowIdx += 1
            colIdx += 1

        rowIdx = queenColIdx - 1
        colIdx = queenRowIdx + 1
        while rowIdx >= 0 and colIdx < self.n:
            if self.chessboard[rowIdx][colIdx] == True:
                return False
            rowIdx -= 1
            colIdx += 1

        rowIdx = queenColIdx + 1
        colIdx = queenRowIdx - 1
        while rowIdx < self.n and colIdx >= 0:
            if self.chessboard[rowIdx][colIdx] == True:
                return False
            rowIdx += 1
            colIdx -= 1
        return True

    def run(self):
        print(self.solveNQueens(4))

foo = Solution()
foo.run()