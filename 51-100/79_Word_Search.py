from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        firstLetter = word[0]
        startPosition = []
        # find first position
        for rowIdx in range(len(board)):
            for colIdx in range(len(board[0])):
                if board[rowIdx][colIdx] == firstLetter:
                    startPosition.append((rowIdx, colIdx))

        for rowIdx, colIdx in startPosition:
            footprint = dict()
            if self.deep(0, word, board, rowIdx, colIdx, footprint):
                return True
        return False

    def deep(self, letterIdx, word, board, rowIdx, colIdx, footprint):
        if rowIdx in footprint and colIdx in footprint[rowIdx]:
            return False
        if board[rowIdx][colIdx] == word[letterIdx]:
            if letterIdx == len(word) - 1:
                return True
            if rowIdx not in footprint:
                footprint[rowIdx] = set()
                footprint[rowIdx].add(colIdx)
            else:
                footprint[rowIdx].add(colIdx)

            if rowIdx - 1 >= 0 and self.deep(letterIdx + 1, word, board, rowIdx - 1, colIdx, footprint):
                return True
            elif rowIdx + 1 < len(board) and self.deep(letterIdx + 1, word, board, rowIdx + 1, colIdx, footprint):
                return True
            if colIdx - 1 >= 0 and self.deep(letterIdx + 1, word, board, rowIdx, colIdx - 1, footprint):
                return True
            if colIdx + 1 < len(board[0]) and self.deep(letterIdx + 1, word, board, rowIdx, colIdx + 1, footprint):
                return True

            footprint[rowIdx].remove(colIdx)
            if len(footprint[rowIdx]) == 0:
                del footprint[rowIdx]
            return False

    def run(self):
        print(self.exist([["A", "B", "C", "E"], [
              "S", "F", "C", "S"], ["A", "D", "E", "E"]], 'ABCCED'))
        print(self.exist([["A", "B", "C", "E"], [
              "S", "F", "C", "S"], ["A", "D", "E", "E"]], 'SEE'))
        print(self.exist([["A", "B", "C", "E"], [
              "S", "F", "C", "S"], ["A", "D", "E", "E"]], 'ABCB'))

        print(self.exist([['a']], 'a'))

foo = Solution()
foo.run()
